from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import Home, signin, logout_view, login_view, profile, edit

urlpatterns = [

    path('', Home.as_view(), name='register'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit, name='edit'),

]

if  settings.DEBUG:

    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

