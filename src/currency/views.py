import csv

from django.http import HttpResponse
from django.views.generic import View

from currency.models import Rate

'''
class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(choices=mch.CURRENCY_CHOICES)
    buy = models.DecimalField(max_digits=4, decimal_places=2)
    sale = models.DecimalField(max_digits=4, decimal_places=2)
    source = models.PositiveSmallIntegerField(choices=mch.SOURCE_CHOICES)
'''

# Create your views here.
class RateCSV(View):
    HEADERS = [
        'id',
        'created',
        'currency',
        'buy',
        'sale',
        'source',
    ]


    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="rates.csv"'
        writer = csv.writer(response)

        writer.writerow(self.HEADERS)

        for rate in Rate.objects.all().iterator():
            row = [
                getattr(rate, f'get_{attr}_display')()
                if hasattr(rate, f'get_{attr}_display') else getattr(rate, attr)
                for attr in self.HEADERS
            ]

            writer.writerow(row)
            # writer.writerow(map(str, [
            #     rate.id,
            #     rate.created,
            #     rate.get_currency_display(),
            #     rate.buy,
            #     rate.sale,
            #     # rate.get_source_display(),
            # ]))

        return response
