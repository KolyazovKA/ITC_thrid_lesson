from datetime import datetime, timezone

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView
from books import filters

from books.models import Book


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

class BookDelete(DeleteView):
    template_name = 'book_shelf/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('books_list')

class NewBooks(ListView):
    template_name = 'book_shelf/new_books.html'
    context_object_name = 'books'
    model = Book