from django.test import TestCase
from django.urls import reverse

from books import factories, models

class BookTestCase(TestCase):
    def setUp(self):
        self.book = factories.BookFactory()
        self.author = factories.AuthorFactory()

    def test_get_book_list(self):
        url = reverse('books_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['books'].count(), models.Book.objects.count())

    def test_get_book_detail(self):
        url = reverse('book_detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        url = reverse('book_delete', kwargs={'pk': self.book.pk})
        old_book_count = models.Book.objects.count()
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_book_count, models.Book.objects.count())

        print(old_book_count, models.Book.objects.count())

    def test_create_book(self):
        url = reverse('book_create')
        old_book_count = models.Book.objects.count()
        response = self.client.post(url, {'title': '123', 'author': self.author.pk, 'published_date': '1809-01-01'})
        self.book.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertGreater(models.Book.objects.count(), old_book_count)

    def test_update_book(self):
        old_title = self.book.title
        url = reverse('book_update', kwargs={'pk': self.book.pk})
        response = self.client.post(url, {'title': 'new_title'})
        self.book.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.book.title, old_title)
