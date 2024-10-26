import json

# JSON data as a string
data_string = '''
{
    "products": [
        {
            "barcode_number": "",
            "barcode_formats": "",
            "mpn": "",
            "model": "",
            "asin": "",
            "title": "",
            "category": "",
            "manufacturer": "",
            "brand": "",
            "contributors": [
                {
                    "role": "",
                    "name": ""
                },
                {
                    "role": "",
                    "name": ""
                }
            ],
            "energy_efficiency_class": "",
            "color": "",
            "gender": "",
            "material": "",
            "pattern": "",
            "format": "",
            "multipack": "",
            "size": "",
            "length": "",
            "width": "",
            "height": "",
            "weight": "",
            "release_date": "",
            "description": "",
            "features": [],
            "images": [],
            "last_update": "",
            "stores": [
                {
                    "name": "",
                    "country": "",
                    "currency": "",
                    "currency_symbol": "",
                    "price": "",
                    "sale_price": "",
                    "tax": [
                        {
                            "country": "",
                            "region": "",
                            "rate": "",
                            "tax_ship": ""
                        }
                    ],
                    "link": "",
                    "item_group_id": "",
                    "availability": "",
                    "condition": "",
                    "shipping": [
                        {
                            "country": "",
                            "region": "",
                            "service": "",
                            "price": ""
                        }
                    ],
                    "last_update": ""
                }
            ],
            "reviews": [
                {
                    "name": "",
                    "rating": "",
                    "title": "",
                    "review": "",
                    "date": ""
                }
            ]
        }
    ]
}
'''

print("Tipo de dato antes de la deserialización: " + str(type(data_string)))

# Deserializando los datos
data = json.loads(data_string)

print("Tipo de dato después de la deserialización: " + str(type(data)))

# Iterar sobre todos los objetos dentro de la lista "products"
for product in data["products"]:
    print("Producto:")
    for key, value in product.items():
        print(f"{key}: {value}")
    print()  # Agrega una línea en blanco entre cada producto


