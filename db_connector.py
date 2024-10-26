# db_connector.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime

# Crear la conexión a la base de datos
DATABASE_URL = 'HERE SHOULD GO THE URL (Hidden to make code public)'
engine = create_engine(DATABASE_URL)

# Definir el modelo para la tabla selling_price
Base = declarative_base()

class SellingPrice(Base):
    __tablename__ = 'selling_price'

    id = Column(Integer, primary_key=True)
    selling_price = Column(Integer)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_on = Column(DateTime)
    time_since_launch = Column(Integer)
    upc_id = Column(Integer, ForeignKey('upc.id'))
    type_id = Column(Integer)
    status_id = Column(Integer)

    # Relación con la tabla upc
    upc = relationship('UPC', back_populates='selling_prices')

# Definir el modelo para la tabla upc
class UPC(Base):
    __tablename__ = 'upc'

    id = Column(Integer, primary_key=True)
    upc = Column(String)
    product_variant_id = Column(Integer)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_on = Column(DateTime)
    launch_date = Column(DateTime)

    # Relación con la tabla selling_price
    selling_prices = relationship('SellingPrice', back_populates='upc')

# Crear la tabla en la base de datos (solo se necesita hacer una vez)
Base.metadata.create_all(engine)
