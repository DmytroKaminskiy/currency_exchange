from uuid import uuid4

import pytest
from rest_framework.reverse import reverse

from account.models import User
from account.tasks import send_activation_code_async
from currency.tasks import _privat


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


@pytest.mark.django_db
def test_task(mocker):
    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = 1
    _privat()


@pytest.mark.django_db
def test_send_email(mocker):
    from django.core import mail
    emails = mail.outbox
    print('EMAILS:', emails)

    send_activation_code_async(1, str(uuid4()))
    emails = mail.outbox
    print('EMAILS', emails)
