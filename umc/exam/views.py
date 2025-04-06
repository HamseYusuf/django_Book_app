from django.shortcuts import render , redirect
from django.http import HttpResponse
from.models import Book , Post
from.forms import BookForm


def create_book(request):
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form' : form
    }
    return render(request , 'create.html' , context)


def book_detail(request , pk):
    book = Book.objects.get(pk = pk)
    context = {
        'book' : book
    }
    return render(request , 'book_detail.html' , context)


def book_update(request , pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_date = request.POST.get('date')
        book.price = request.POST.get('price')
        book.save()
        return redirect('home')
    context = {
        'book' : book
    }
    return render(request , 'book_update.html' , context)

def book_delete(request , pk):
    book = Book.objects.get(pk = pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request , 'book_delete.html')

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request , 'post.html', context)



def home(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request , 'home.html' , context)

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')

def login(request):
    return render(request, 'login.html')
def email(request):
    return render(request, 'email.html')

def signup(request):
    return render(request, 'signup.html')