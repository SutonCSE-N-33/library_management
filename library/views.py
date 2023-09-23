from django.shortcuts import render,get_object_or_404, redirect
from .models import Book,ReviewRating
from category.models import Category
from borrowing_and_returning.models import BookItem,Book
from django.core.paginator import Paginator
from .forms import ReviewForm
# Create your views here.
def library(request,category_slug=None):
    if category_slug : 
        category = get_object_or_404(Category, slug = category_slug)
        books = Book.objects.filter(is_available = True, category=category)
        page = request.GET.get('page')
        paginator = Paginator(books, 3)
        paged_book = paginator.get_page(page)
        
    elif request.method == 'POST':
        data = request.POST
        title = data.get('title')
        books = Book.objects.filter(is_available = True,title__icontains=title)
        page = request.GET.get('page')
        paginator = Paginator(books, 3)
        paged_book = paginator.get_page(page)
    else:
        books = Book.objects.filter(is_available = True)
        paginator = Paginator(books, 9)
        page = request.GET.get('page')
        paged_book = paginator.get_page(page)
        
        
        
    categories = Category.objects.all()
    context = {'books' : paged_book, 'categories' : categories, }
    
    return render(request,'library/books.html',context)




def book_detail(request, category_slug, book_slug):
    single_book = Book.objects.get(slug = book_slug, category__slug = category_slug)
    reviews = ReviewRating.objects.filter(book=single_book)
    
    return render(request,'library/book-detail.html',{'book':single_book,'reviews':reviews})



def submit_review(request, book_id, item_id):
    form = ReviewForm()
    if request.method == 'POST':
            form = ReviewForm(request.POST)
            book = Book.objects.get(id = book_id)
            remove_book = get_object_or_404(Book, id=book_id)
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.book = book
                data.user = request.user
                data.save()
                
                if request.user.is_authenticated:
                    cart_item = BookItem.objects.get(book=remove_book, user=request.user, id=item_id)
                    remove_book = Book.objects.get(id=book_id)
                    remove_book.stock += 1
                    remove_book.save()
                    if book.is_available == False:
                        remove_book.is_available=True
                        remove_book.save()
                        
                cart_item.delete()
                return redirect('cart')
                
    return render(request, 'library/review.html',{'form':form})
