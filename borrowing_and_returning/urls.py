from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.cart, name='cart'),
    path('<int:book_id>/', views.add_to_cart, name='add_cart'),
    path('added/',views.borrowing, name='borrowed'),
    path('remove/<int:book_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
]