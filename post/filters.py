import django_filters
from core import models

class MyModelFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    category = django_filters.CharFilter(field_name ='Category', lookup_expr ='exact')
    author = django_filters.CharFilter(field_name ='author', lookup_expr ='exact')
    class Meta:
        model = models.Post
        fields = ['start_date', 'end_date']
