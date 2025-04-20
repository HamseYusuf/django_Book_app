from django.shortcuts import redirect , render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView, FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login , logout
from .models import Book, Post
from .forms import BookForm


class HomeView(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'



class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        print(form.get_user())
        return redirect('home')


class CustomLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

    def get(self, request, *args, **kwargs):
        return render(request, 'logout.html')


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class BookCreateView(LoginRequiredMixin,CreateView):
    model = Book
    form_class = BookForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BookDetailView(LoginRequiredMixin,DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_update.html'
    success_url = reverse_lazy('home')


class BookDeleteView(LoginRequiredMixin,DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home')



class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'
