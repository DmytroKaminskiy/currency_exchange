import django_filters
from django.forms import DateInput, DateTimeInput

from currency.models import Rate


class RateFilter(django_filters.FilterSet):
    created_date = django_filters.DateFilter(
        field_name='created',
        lookup_expr='date',
        widget=DateInput(
            attrs={
                'class': 'datepicker',
                'type': 'date',
            }
        ))
    # created_dt = django_filters.DateTimeFilter(
    #     field_name='created',
    #     widget=DateTimeInput(
    #         attrs={
    #             'class': 'datetimepicker',
    #             'type': 'datetime',
    #         }
    #     ))

    class Meta:
        model = Rate
        fields = [
            'buy',
            'sale',
            'source',
            'created_date',
            # 'created_dt',
        ]
