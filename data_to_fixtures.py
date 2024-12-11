import json

# load the JSON data
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# mapping of the models to the JSON keys
model_mapping = {
    "credit_cards": "plm.creditcards",
    "clients": "plm.clients",
    "delivery_options": "plm.deliveryoptions",
    "orders": "plm.orders",
    "items": "plm.items",
    "is_composed": "plm.iscomposed",
    "warehouses": "plm.warehouses",
    "stocked": "plm.stocked",
    "contact": "plm.contact",
    "admins": "plm.admins"
}

fixtures = []

# convert the JSON data into Django fixtures
for key, model in model_mapping.items():
    for index, entry in enumerate(data.get(key, []), start=1):
        fixture = {
            "model": model,
            "pk": index,
            "fields": entry
        }
        fixtures.append(fixture)

# save the fixtures to a JSON file
with open('fixtures.json', 'w', encoding='utf-8') as output_file:
    json.dump(fixtures, output_file, ensure_ascii=False, indent=4)
