import pytest
from rest_framework.reverse import reverse

from account.models import User


def test_sanity():
    assert 200 == 200
    # assert 200 == 201


@pytest.mark.django_db
def test_get_rates_list(api_client):
    response = api_client.get(reverse('api-currency:rates'))
    assert response.status_code == 401

    username = 'srjgdrjgdkr@mail.com'
    password = '1234567'
    user = User.objects.create(username=username, email=username)
    user.set_password(password)
    user.save()

    api_client.login(username=username, password=password)
    response = api_client.get(reverse('api-currency:rates'))
    assert response.status_code == 200

    response = api_client.post(reverse('api-currency:rates'), data={}, format='json')
    print(response.json())
    assert response.status_code == 400


@pytest.mark.django_db
def test_csv_rates(client):
    response = client.get(reverse('currency:download-rates'))
    assert response.status_code == 200
