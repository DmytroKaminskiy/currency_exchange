from django.urls import path

from currency.api import views

app_name = 'api-currency'

urlpatterns = [
    path('rates/', views.RatesView.as_view(), name='rates'),
    path('rates/<int:pk>/', views.RateView.as_view(), name='rate'),
]
# api/v1/currency/rates/
