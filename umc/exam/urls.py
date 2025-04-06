from django.urls import path
from .views import home , about , contact , login , email , signup , post_list , create_book , book_detail , book_update , book_delete

urlpatterns = [
    path('' , home , name="home"),
    path('about/' , about , name="about"),
    path('contact/' , contact , name="contact"),
    path('login/', login, name="login"),
    path('email/', email, name="email"),
    path('signup/', signup, name="signup"),
    path('posts' , post_list , name="posts"),
    path('create' , create_book , name="create"),
    path('book/<int:pk>/' , book_detail , name="book_detail"),
    path('update/<int:pk>/' , book_update , name="book_update"),
    path('delete/<int:pk>/' , book_delete , name="book_delete")

]