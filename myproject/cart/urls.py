# cart/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<str:item>/', views.IndexView.as_view(), name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('kill_session/', views.kill_session, name='kill_session'),
]
