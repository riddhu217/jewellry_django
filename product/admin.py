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
    list_display = ('p_name', 'category_id','p_price','stock')
    search_fields = ('p_name', 'category_id')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Product, ProductAdmin)
