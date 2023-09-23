from django.contrib import admin
from . models import Book,ReviewRating
# Register your models here.
class BookAdmin(admin.ModelAdmin): # admin panel customize korte modeladmin use kori
     list_display = ['title', 'author', 'details','publication_date','isbn','stock','category' ,'created_date', 'modified_date', 'is_available']
     
     prepopulated_fields = {'slug' : ('title',)}
     
admin.site.register(Book, BookAdmin)

admin.site.register(ReviewRating)
