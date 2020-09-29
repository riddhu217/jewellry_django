from django.contrib import admin
from .models import Product, ProductImage, Category, Brand, Order, OrderItem, Cart, CartItem, FeedBack

# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(OrderItem)


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    can_delete = True
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'ProductImage'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','status','total')
    search_fields = ('status','total')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Order, OrderAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','product','quantity')
    search_fields = ('status','total')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CartItem, CartItemAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'contact_no','feedback')
    search_fields = ('name', 'city')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(FeedBack, FeedbackAdmin)