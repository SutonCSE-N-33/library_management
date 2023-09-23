from django.shortcuts import render
from library.models import Book
from django.core.paginator import Paginator


def home(request,book_items=None):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        books = Book.objects.filter(is_available = True,title__icontains=title)
        page = request.GET.get('page')
        paginator = Paginator(books, 3)
        paged_book = paginator.get_page(page)
        
    else:
         books = Book.objects.filter(is_available = True)
         paginator = Paginator(books, 12)
         page = request.GET.get('page')
         paged_book = paginator.get_page(page)
   
    
    return render(request,'index.html',{'books':paged_book})