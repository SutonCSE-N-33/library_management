from django.db import models
from library.models import Book
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length = 250, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.cart_id
    
    
class BookItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null = True)
    
    
    def __str__(self):
        return str(self.book)
