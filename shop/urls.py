from django.urls import path
from . import views  # Importer les vues depuis le même module

urlpatterns = [
    path('', views.index, name='home'),  # Utiliser views.index au lieu de index
    
    path('<int:myid>/', views.detail, name="detail"),  # Utiliser views.detail au lieu de detail
    path('checkout/', views.checkout, name="checkout"),
    path('confirmation/', views.confimation, name="confirmation" ),
]
