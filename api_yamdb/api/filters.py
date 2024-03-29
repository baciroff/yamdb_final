from django_filters import rest_framework as filters
from reviews.models import Title


class TitleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')
    year = filters.NumberFilter(field_name='year')
    rating = filters.CharFilter(field_name='rating__slug')

    class Meta:
        model = Title
        fields = ['name', 'year', 'genre', 'category', 'rating']
