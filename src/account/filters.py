import django_filters

from currency.models import Rate


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = ['sale', 'source', 'created', ]
