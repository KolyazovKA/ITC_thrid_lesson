from datetime import datetime, timezone

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from django_filters.views import FilterView
from books import filters
from rest_framework import viewsets

from books.models import Book, Author, Review, Storage
from books import serializers


class AuthorAPI(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.Author

class BookAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.Book

class ReviewAPI(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = serializers.Review

class StorageAPI(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = serializers.Storage

class BookListTemplateView(TemplateView):
    template_name = 'book_shelf/book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


class BookList(FilterView):
    template_name = 'book_shelf/book_list.html'
    model = Book
    context_object_name = 'books'
    filterset_class = filters.Books


class BookDetail(DetailView):
    template_name = 'book_shelf/book_detail.html'
    model = Book
    context_object_name = 'book'


class BookUpdate(UpdateView):
    template_name = 'book_shelf/book_form.html'
    model = Book
    fields = ['title', 'author', 'published_date']

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.object.pk})


class BookCreate(CreateView):
    template_name = 'book_shelf/book_form.html'
    model = Book
    fields = ['title', 'author', 'published_date']

    def get_success_url(self):
        return reverse_lazy('books_list')


class BookDelete(DeleteView):
    template_name = 'book_shelf/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('books_list')


class NewBooks(ListView):
    template_name = 'book_shelf/new_books.html'
    context_object_name = 'books'
    model = Book
