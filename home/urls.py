from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('home/', views.home,name='home'),
    path('clientes/', include('clientes.urls')),
    
    

]
