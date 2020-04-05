import pytest
from django.urls import reverse

from account.models import User


def test_sanity():
    assert 200 == 200


def test_index_page(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


def test_rates_not_auth(client):
    url = reverse('api-currency:rates')
    response = client.get(url)
    assert response.status_code == 401
    resp_j = response.json()
    assert len(resp_j) == 1
    assert resp_j['detail'] == 'Authentication credentials were not provided.'


def test_rates_auth(api_client, user):
    url = reverse('api-currency:rates')
    response = api_client.get(url)
    assert response.status_code == 401

    api_client.login(user.username, user.raw_password)
    response = api_client.get(url)
    assert response.status_code == 200


def test_get_rates(api_client, user):
    url = reverse('api-currency:rates')
    api_client.login(user.email, user.raw_password)
    response = api_client.get(url)
    assert response.status_code == 200

    # response = api_client.post(url, data={}, format='json')

    # response = api_client.put(url + id, data={}, format='json')
    # response = api_client.delete(url + id, data={}, format='json')


class Response:
    pass


def test_task(mocker):
    from currency.tasks import _privat

    def mock():
        response = Response()
        response.json = lambda: [{'ccy': 'USD'}]
        return response

    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = mock()

    _privat()

def test_send_email():
    from django.core import mail
    from account.tasks import send_activation_code_async
    from uuid import uuid4

    emails = mail.outbox
    print('EMAILS:', emails)

    send_activation_code_async.delay(1, str(uuid4()))
    emails = mail.outbox
    assert len(emails) == 1

    email = mail.outbox[0]
    assert email.subject == 'Your activation code'


def test_smoke(client):
    response = client.get(reverse('account:smoke'))
    assert response.status_code == 200

# tests for ContactUs API, GET list, create (POST), for object [GET, PUT, PATCH, DELETE]
# test _privat, _mono

# 0. email = 'awdawdawdaw@mail.com'
# 1. client.post('/registration/'. data={email: email})
# 2. User.objects.get(email=email).uuid, emails = mail.outbox.
# 3. client.post('/registration/complete/'. data={uuid: uuid})
# 4. user LOGIN!
