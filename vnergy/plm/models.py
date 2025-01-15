from django.db import models

class CreditCards(models.Model):
    card = models.CharField(max_length=16, primary_key=True)
    expiry_date = models.DateField()

class Clients(models.Model):
    email = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    card = models.ForeignKey(CreditCards, on_delete=models.CASCADE)

class DeliveryOptions(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    delivery_date = models.DateField()
    delivery_address = models.CharField(max_length=50)
    delivery_postal_code = models.CharField(max_length=5)
    option = models.CharField(max_length=8, choices=[('Standard', 'Standard'), ('Express', 'Express')])

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('In transit', 'In transit'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')])
    email = models.ForeignKey(Clients, on_delete=models.CASCADE)
    card = models.ForeignKey(CreditCards, on_delete=models.CASCADE)
    delivery_id = models.ForeignKey(DeliveryOptions, on_delete=models.CASCADE)

class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class IsComposed(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('order_id', 'item_id')

class Warehouses(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    max_capacity = models.IntegerField()

class Stocked(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(Warehouses, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('item_id', 'warehouse_id')

class Admins(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=12, choices=[('Admin', 'Admin'), ('Data Analyst', 'Data Analyst'), ('Manager', 'Manager'), ('Employee', 'Employee')])

class Suppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    product_sold = models.TextField()

class IsSupplied(models.Model):
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('supplier_id', 'item_id')

class CustomerFeedbacks(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    feedback_type = models.CharField(max_length=50, choices=[('Review', 'Review'), ('Complaint', 'Complaint')])
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(blank=True, null=True)
    answer_date = models.DateTimeField(blank=True, null=True)
