from django.contrib import admin
from .models import Product, Order

# Registro do Produto no admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # Campos exibidos na lista
    search_fields = ('name', 'description')          # Campos pesquisáveis
    list_filter = ('price',)                          # Filtro por preço

# Registro do Pedido no admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('product__name', 'user__username')
    readonly_fields = ('created_at',)
