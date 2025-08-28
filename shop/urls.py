from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from .views import list, orders, add_to_cart, detail
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),       # Página da loja / produtos
    path('list/<int:pk>/', views.detail, name='detail'),
    path('profile/orders/', views.orders, name='orders'),  # Pedidos do usuário
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Adicionar ao carrinho
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
        