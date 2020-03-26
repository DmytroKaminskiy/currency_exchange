from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from currency_exchange import settings WRONG!
from django.conf import settings

API_PREFIX = 'api/v1'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),

    path('account/', include('account.urls')),
    path('currency/', include('currency.urls')),

    # API
    path(f'{API_PREFIX}/currency/', include('currency.api.urls')),
    path(f'{API_PREFIX}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_PREFIX}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# SWAGGER
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='DOCS')

urlpatterns.append(path(f'{API_PREFIX}/docs/', schema_view))

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg2NDU5MzQxLCJqdGkiOiIxZTJjNjAxMjBmNjc0MmFmYmIwNmFkYjBkYTJkODc1OCIsInVzZXJfaWQiOjh9.PScH_ZKujjlF8zJyGWGVC7_DjxVscm843Aog2YW9838
# Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg2NDU5MzQxLCJqdGkiOiIxZTJjNjAxMjBmNjc0MmFmYmIwNmFkYjBkYTJkODc1OCIsInVzZXJfaWQiOjh9.PScH_ZKujjlF8zJyGWGVC7_DjxVscm843Aog2YW9838