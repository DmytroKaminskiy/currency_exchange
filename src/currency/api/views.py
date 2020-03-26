from rest_framework import generics

from currency.api.serializers import RateSerializer
from currency.models import Rate


class RatesView(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    # queryset = Rate.objects.all()[:20] WRONG

    # useful for 2
    # def get_queryset(self):
    # self.request.user
    #     pass


class RateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

#  filters - https://django-filter.readthedocs.io/en/master/
'''
1.
http://127.0.0.1:8000/api/v1/currency/rates/?created__lt=10/10/2019

'created' - exact, lt, lte, gt, gte + BONUS range
'currency', - exact
'source', - exact

2. account.model.Contact - /contacts/ - GET, POST
                           /contacts/<id>/ - GET, PUT
                           list only auth users (request.user)
                           send email after create (/contacts/id/ POST)
                   
3. BONUS
ADD TESTS for API
self.client.get('api/v1/currency/rates/') -> json
self.client.post('api/v1/currency/rates/', data={}) -> json['id']
self.client.get('api/v1/currency/rates/json['id']') -> status_code == 200
'''
