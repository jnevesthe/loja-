from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product, Order

# Lista de produtos na loja (sem login obrigatório)
def list(request):
    products = Product.objects.all()
    return render(request, 'shop/list.html', {'products': products})

# Página de pedidos do usuário (login obrigatório)
@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/orders.html', {'orders': orders})

# Adicionar produto ao pedido via AJAX (login obrigatório)
@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        order, created = Order.objects.get_or_create(
            user=request.user,
            product=product,
            status='Pendente'
        )
        if not created:
            order.quantity += 1
            order.save()
        else:
            order.quantity = 1
            order.save()
        return JsonResponse({'success': True, 'product': product.name, 'quantity': order.quantity})
    return JsonResponse({'success': False, 'error': 'Método inválido'})

# Página de detalhes do produto
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/detail.html', {'product': product})