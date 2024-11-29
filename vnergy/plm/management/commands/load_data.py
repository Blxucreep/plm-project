from django.core.management.base import BaseCommand
from django.db import transaction
from plm.models import *

import json

class Command(BaseCommand):
    help = 'Load data from JSON file'

    def handle(self, *args, **options):
        file_path = 'data.json'

        with open(file_path) as f:
            data = json.load(f)

        self.load_data(Client, data.get('order_client', []))
        self.load_data(Order, data.get('order_order', []))
        self.load_data(Product, data.get('order_product', []))
        self.load_data(Fruit, data.get('order_fruit', []))
        self.load_data(Vegetable, data.get('order_vegetable', []))
        self.load_data(OrderDetail, data.get('order_orderdetail', []))
        self.load_data(Warehouse, data.get('order_warehouse', []))

    @transaction.atomic
    def load_data(self, model, data_list):
        unique_fields = {
            'Client': 'email',
            'Contact': 'contact_id',
            'Order': 'order_id',
            'Product': 'product_id',
            'Fruit': 'fruit_id',
            'Vegetable': 'vegetable_id',
            'OrderDetail': 'orderdetail_id',
            'Warehouse': 'warehouse_id',
            'Stock': 'stock_id',
        }

        model_name = model.__name__
        unique_field = unique_fields.get(model_name)

        if unique_field is None:
            self.stdout.write(self.style.ERROR(f'Unique field not defined for {model_name}'))
            return

        existing_entries = model.objects.filter(**{f'{unique_field}__in': [entry[unique_field] for entry in data_list]})
        existing_ids = set(getattr(entry, unique_field) for entry in existing_entries)

        new_entries = []

        for entry in data_list:
            if entry[unique_field] not in existing_ids:
                new_entries.append(model(**entry))

        if new_entries:
            model.objects.bulk_create(new_entries)
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(new_entries)} entries for {model_name}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'No new entries for {model_name}'))
