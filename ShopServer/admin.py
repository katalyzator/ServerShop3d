from django.contrib import admin

from ShopServer.models import Product, CategoryProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'active']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryProduct, CategoryAdmin)
