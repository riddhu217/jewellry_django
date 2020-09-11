from django.contrib import admin
from .models import Product, ProductImage, Category, Brand, Order, OrderItem, Cart, CartItem, FeedBack

# Register your models here.


admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(FeedBack)


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    can_delete = True
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'ProductImage'


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLine, ]


admin.site.register(Product, ProductAdmin)
