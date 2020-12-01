from django.contrib import admin
from .models import Product, ProductImage, Category, Brand, Order, OrderItem, Cart, CartItem, FeedBack, BillingAddress
import csv
from django.http import HttpResponse

# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)

#product
def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="product.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "p_name",
        "category_id",
        "brand_id",
        "stock",
        "p_desc",
        "p_price",
        "discount",
    ])
    for obj in queryset:
        writer.writerow([
            obj.p_name,
            obj.category_id,
            obj.brand_id,
            obj.stock,
            obj.p_desc,
            obj.p_price,
            obj.discount
        ])
    return response

#Orderitem

def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="orderitem.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "order",
        "product",
        "quantity",
    ])
    for obj in queryset:
        writer.writerow([
            obj.order,
            obj.product,
            obj.quantity,
        ])
    return response


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('Order', 'product', 'quantity')
    search_fields = ('quantity', 'product')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    actions = [export_csv]


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
    actions = [export_csv]


admin.site.register(Product,ProductAdmin)

def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="order.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "user",
        "order_date",
        "status",
        "total"
    ])
    for obj in queryset:
        writer.writerow([
            obj.user,
            obj.order_date,
            obj.status,
            obj.total,
        ])
    return response

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','status','total')
    search_fields = ('status','total')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    actions = [export_csv]


admin.site.register(Order, OrderAdmin)

#cartitem
def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="cartitem.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "cart",
        "product",
        "quantity",
    ])
    for obj in queryset:
        writer.writerow([
            obj.cart,
            obj.product,
            obj.quantity,
             ])
    return response


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','product','quantity')
    search_fields = ('status','total')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    actions = [export_csv]


admin.site.register(CartItem, CartItemAdmin)

#feedback


def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="feedback.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "name",
        "city",
        "contact_no",
        "feedback",
    ])
    for obj in queryset:
        writer.writerow([
            obj.name,
            obj.city,
            obj.contact_no,
            obj.feedback
             ])
    return response


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'contact_no','feedback')
    search_fields = ('name', 'city')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    actions = [export_csv]


admin.site.register(FeedBack, FeedbackAdmin)

def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="billing_address.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "fname",
        "lname",
        "Address",
        "city",
        "zip",
        "state",
        "contact_no",
        "email",
    ])
    for obj in queryset:
        writer.writerow([
            obj.fname,
            obj.lname,
            obj.Address,
            obj.city,
            obj.zip,
            obj.state,
            obj.contact_no,
            obj.email,
             ])
    return response


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','Address', 'city', 'contact_no','zip')
    search_fields = ('fname', 'city')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    actions = [export_csv]


admin.site.register(BillingAddress, BillingAddressAdmin)