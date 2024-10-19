import django_filters
import books.models
from django.db.models import Q

class Books(django_filters.FilterSet):
    # Фильтры из урока
    price_range = django_filters.RangeFilter(field_name='storage__price', label='Цена от и до')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains', label='Автор')
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    available = django_filters.BooleanFilter(method='filter_available', label='В наличии')
    term = django_filters.CharFilter(method='filter_term', label='')

    # Мой фильтр
    new_books = django_filters.BooleanFilter(method='filter_new_books', label='Только новые книги')

    class Meta:
        model = books.models.Book
        fields = ['term', 'published_date']

    def filter_available(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(storage__amount__gt=0)

        return queryset.filter(storage__amount=0)

    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(title__icontains=term) | Q(author__name__icontains=term)

        return queryset.filter(criteria).distinct()

    def filter_new_books(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(published_date__gt='2022-12-1')