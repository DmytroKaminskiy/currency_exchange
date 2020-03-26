# from django.conf.urls import path
from django.urls import path

from currency.api.views import CurrenciesView

app_name = 'api-currency'

urlpatterns = [
    path(r'rates/', CurrenciesView.as_view(), name='rates'),
]
