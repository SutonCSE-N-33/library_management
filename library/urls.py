from django.urls import path
from . import views

urlpatterns = [
    path('',views.library,name='books'),
    path('category/<slug:category_slug>/', views.library, name='books_by_category'),
    path('search/', views.library, name='books_by_filter'),
    path('<slug:category_slug>/<slug:book_slug>/', views.book_detail, name='book_detail'),
    path('review/<int:book_id>/<int:item_id>/', views.submit_review, name='submit_review'),
]

