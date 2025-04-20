from django.urls import path
from .views import (
    HomeView, CustomLoginView, CustomLogoutView, SignupView,
    BookCreateView, BookDetailView, BookUpdateView, BookDeleteView,
    PostListView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('posts/', PostListView.as_view(), name='post'),
]
