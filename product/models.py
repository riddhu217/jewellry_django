from django.db import models

# Create your models here.
from account.models import CustomUser


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_type = models.CharField(max_length=100)


class Product(models.Model):
    p_name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.IntegerField()
    p_desc = models.CharField(max_length=300)
    p_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.CharField(max_length=10)

    def __str__(self):
        return self.p_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Order(models.Model):
    CREATED = 'created'
    CANCELED = 'canceled'
    COMPLETED = 'completed'

    STATUS_CHOICES = (
        (CREATED, 'Order Created'),
        (CANCELED, 'Order Canceled'),
        (COMPLETED, 'Order Completed'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=CREATED)
    total = models.DecimalField(max_digits=10, decimal_places=2)


class OrderItem(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class FeedBack(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    feedback = models.TextField()
