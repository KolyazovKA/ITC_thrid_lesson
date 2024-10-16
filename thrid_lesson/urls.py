"""
URL configuration for thrid_lesson project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books_list_template_view/', views.BookListTemplateView.as_view(), name='book_list_template_view'),
    path('books_list/', views.BookList.as_view(), name='books_list'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('book/new/', views.NewBooks.as_view(), name='new_books')
]
