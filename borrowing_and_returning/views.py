from django.shortcuts import render,redirect,get_object_or_404
from library.models import Book
from .models import Cart, BookItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, book_id):
    current_user = request.user
    book = Book.objects.get(id=book_id) #get the product
    # If the user is authenticated
    if current_user.is_authenticated:
        is_cart_item_exists = BookItem.objects.filter(book=book, user=current_user).exists()
        if is_cart_item_exists:
            return redirect('borrowed')
        else:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
                if book.stock > 0:
                    book_item = BookItem.objects.create(
                    book = book,
                    cart = cart,
                    user = current_user
                    )
                    book_item.save()
                    book.stock -= 1
                    book.save()
                    if book.stock <= 0:
                        book.is_available=False 
                        book.save()
       
            except Cart.DoesNotExist:
                print('hello','I am except')
                cart = Cart.objects.create(
                    cart_id = _cart_id(request)
                )
                cart.save()
                if book.stock > 0:
                    book_item = BookItem.objects.create(
                    book = book,
                    cart = cart,
                    user = current_user
                    )
                    book_item.save()
                    book.stock -= 1
                    book.save()
                    if book.stock <= 0:
                        book.is_available=False 
                        book.save()
                
            return redirect('cart')                 
    else:
        return  redirect('login')
    
    

def remove_cart_item(request, book_id, cart_item_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user.is_authenticated:
        cart_item = BookItem.objects.get(book=book, user=request.user, id=cart_item_id)
        book = Book.objects.get(id=book_id)
        book.stock += 1
        book.save()
        if book.is_available == False:
            book.is_available=True
            book.save()
    cart_item.delete()
    return redirect('cart')




def cart(request,book_items=None):
    add_book="Please borrow your Necessary Books"
    try:
        if request.user.is_authenticated:
            book_items = BookItem.objects.filter(user=request.user)
        else:
            return redirect('login')
    except ObjectDoesNotExist:
        pass
    
    return render(request, 'cart/cart.html', {'book_items':book_items,'add_book':add_book})


def borrowing(request):
    return render(request,'cart/borrowed.html')
