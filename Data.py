import requests
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime

# Crear la base declarativa
Base = declarative_base()

# Definir la clase Product
class Product(Base):
    __tablename__ = 'product'
 #(Extra data of db hidden to make code public)
    id = Column(Integer, primary_key=True)
    mpn = Column(String)
    model = Column(String)
    asin = Column(String)
    category = Column(String)
    manufacturer = Column(String)
    brand = Column(String)
    energy_efficiency_class = Column(String)
    color = Column(String)
    material = Column(String)
    last_update = Column(DateTime)
    images = Column(String)
    type_id = Column(Enum('new', 'refurbished_A', 'refurbished_B', 'refurbished_C', 'used', 'display'))
    status_id = Column(Enum('Active', 'Inactive'))
    shop_id = Column(Integer, ForeignKey('shop.id'))
    upc_id = Column(Integer, ForeignKey('upc.id'))
    price = Column(Float)
    availability = Column(String)

    shop = relationship("Shop", back_populates="product")
    upc = relationship("Upc", back_populates="product")

    @classmethod
    def from_api(cls, data):

        # Mapear los datos del JSON a las columnas de la clase Product
        product_data = {
            "mpn": data.get("mpn"),
            "model": data.get("model"),
            "asin": data.get("asin"),
            "category": data.get("category"),
            "manufacturer": data.get("manufacturer"),
            "brand": data.get("brand"),
            "last_update": datetime.now() if data.get("last_update") is None else data.get("last_update"),
            "images" : data.get("images"),
            "type_id": "new",  # Valor por defecto
            "status_id": "Active",  # Valor por defecto
            # Añadir más campos según sea necesario
            "price": None,  # Inicializar el precio como None
            "availability": data.get("availability")
        }

        # Recorrer las tiendas asociadas a este producto para obtener el precio
        for store_data in data.get("stores", []):
            price_str = store_data.get("price")
            if price_str:
                # Convertir el precio a float y asignarlo al campo price
                product_data["price"] = float(price_str)
                # Si se encuentra un precio, se detiene el bucle
                break

        return cls(**product_data)

# Definir la clase Shop
class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    currency = Column(String)
    link = Column(String)
    condition = Column(String)
 #(Extra data hidden to make code public)
    product = relationship("Product", back_populates="shop")

    @classmethod
    def from_api(cls, data):
        # Mapear los datos del JSON a las columnas de la clase Shop
        shop_data = {
            "name": data.get("name"),
            "country": data.get("country"),
            "currency": data.get("currency"),
            "link": data.get("link"),
            "condition": data.get("condition"),
          #(Extra data hidden to make code public)
            # Añadir más campos según sea necesario
        }
        return cls(**shop_data)

# Definir la clase Upc
class Upc(Base):
    __tablename__ = 'upc'

    id = Column(Integer, primary_key=True)
    upc = Column(String)
    product_variant_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
    release_date = Column(DateTime)

    product = relationship("Product", back_populates="upc")

    @classmethod
    def from_api(cls, data):
        # Mapear los datos del JSON a las columnas de la clase Upc
        upc_data = {
            "upc": data.get("barcode_number"),
            "product_variant_name": data.get("title"),
            # Añadir más campos según sea necesario

        }
        release_date = data.get("release_date")
        if release_date:
            upc_data["release_date"] = release_date

        return cls(**upc_data)

# Configura la conexión a la base de datos
engine = create_engine('(Hidden to make code public)')
Session = sessionmaker(bind=engine)
session = Session()

# Obtener la lista de todos los UPC disponibles
url = "(Hidden to make code public)"
params = {
    "barcode": "",
    "formatted": "0",  # No formatear la respuesta en JSON
      "key": "(Hidden to make code public)",  # Clave de API aquí
}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    products = data.get("products", [])

# Obtener la lista de todos los productos del JSON
products = data.get("products", [])

# Recorrer los productos y agregarlos a la base de datos
for product_data in products:
  #(Extra data hidden to make code public)
    # Verificar si el UPC ya existe en la tabla Upc o en la columna upc de la tabla Product
    upc_code = product_data.get("barcode_number")
    existing_upc = session.query(Upc).filter_by(upc=upc_code).first()
    existing_product_with_upc = session.query(Product).filter_by(upc_id=existing_upc.id).first() if existing_upc else None

    if existing_upc:
        print(f"El UPC {upc_code} ya existe en la base de datos en la tabla upc.")
    else:
        # Crear una instancia de Upc solo si no existe
        new_upc = Upc.from_api(product_data)
        session.add(new_upc)
        session.commit()
        print(f"UPC con código {new_upc.upc} añadido correctamente a la tabla upc.")

    # Recorrer las tiendas asociadas a este producto
    for store_data in product_data.get("stores", []):
        # Crear una nueva instancia de Shop o recuperar la existente
        existing_shop = session.query(Shop).filter_by(name=store_data.get("name")).first()
        if existing_shop is None:
            new_shop = Shop.from_api(store_data)
            session.add(new_shop)
            session.commit()
        else:
            new_shop = existing_shop

        if existing_product_with_upc:
            print(f"Ya existe un producto con UPC {existing_product_with_upc.upc_id}, mismo precio y misma tienda.")
        else:
            # Crear una instancia de Producto asociada a la tienda
            new_product = Product.from_api(product_data)
            new_product.shop_id = new_shop.id  # Asignar el shop_id correspondiente
            if not existing_upc:  # Verificar si se creó un nuevo UPC
                new_product.upc_id = new_upc.id  # Asignar el id del nuevo upc
            else:
                new_product.upc_id = existing_upc.id  # Asignar el id del upc existente

            # Verificar si ya existe un producto con las mismas condiciones
            existing_product = session.query(Product).filter(
                Product.upc_id == new_product.upc_id,
                Product.shop_id == new_product.shop_id,
                Product.price == new_product.price
            ).first()

            if existing_product is None:
                # Si no existe un producto con las mismas condiciones, se agrega un nuevo producto
                session.add(new_product)
                session.commit()
                print(f"Producto con UPC_id {new_product.upc_id} añadido correctamente.")
# Verificar los UPCs que no tienen ningún producto asociado y crear productos con shop_id null para ellos
for upc_code in session.query(Upc).distinct(Upc.upc):
    existing_product_with_upc = session.query(Product).filter_by(upc_id=upc_code.id).first()

    if not existing_product_with_upc:
        # Obtener los datos del primer UPC coincidente
        product_data = next((prod for prod in products if prod.get("barcode_number") == upc_code.upc), None)
        if product_data:
            # Crear una instancia de Producto con shop_id null
            new_product = Product.from_api(product_data)
            new_product.shop_id = None
            new_product.upc_id = upc_code.id

            # Agregar el nuevo producto
            session.add(new_product)
            session.commit()
            print(f"Producto con UPC {upc_code.upc} y shop_id null añadido correctamente.")
# Cierra la sesión
session.close()
