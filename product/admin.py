from django.contrib import admin
from .models import Product, ProductImage, Category, Brand, Order, OrderItem, Cart, CartItem, FeedBack, BillingAddress

# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('Order', 'product', 'quantity')
    search_fields = ('quantity', 'product')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(OrderItem, OrderItemAdmin)


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    can_delete = True
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'ProductImage'


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('p_name', 'p_price', 'category_id','stock')
    search_fields = ('p_name', 'p_price')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    inlines = [ProductImageInLine,]


admin.site.register(Product,ProductAdmin)


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


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','Address', 'city', 'contact_no','zip')
    search_fields = ('fname', 'city')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(BillingAddress, BillingAddressAdmin)