from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from book.forms import BookForm
from book.models import Book


def add_book(request):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('my_login')
    form = BookForm()
    if request.method=="POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print("true")
            form.save()
            return redirect('book_list')
        else:
            print("fail")

    context={'form':form}
    return render(request, 'back/add_book.html', context)

def book_list(request):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('my_login')
    books=Book.objects.all()
    context = {'books': books}
    return render(request, 'back/book_list.html', context)

def update_book(request):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('my_login')
    form = BookForm()
    context = {'form': form}
    return render(request, 'back/update_book.html', context)

def delete_book(request,pk):
    # check user authenticated or not
    if not request.user.is_authenticated:
        return redirect('my_login')
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('book_list')