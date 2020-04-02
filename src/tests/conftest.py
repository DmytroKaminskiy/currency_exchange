import pytest

from django.urls import reverse
from pytest_django.fixtures import _django_db_fixture_helper

from rest_framework.test import APIClient


@pytest.fixture(scope='session')
def db_session(request, django_db_setup, django_db_blocker):
    """
    Changed scope to 'session'
    """
    if 'django_db_reset_sequences' in request.funcargnames:
        request.getfixturevalue('django_db_reset_sequences')
    if 'transactional_db' in request.funcargnames \
            or 'live_server' in request.funcargnames:
        request.getfixturevalue('transactional_db')
    else:
        _django_db_fixture_helper(request, django_db_blocker, transactional=False)


@pytest.fixture(scope='session')
def api_client():

    client = APIClient()

    def login(username, password, headers=None):
        r = client.post(reverse('token_obtain_pair'),
                        data=dict(username=username, password=password),
                        headers=headers)
        assert r.status_code == 200, r.content
        assert "access" in r.json(), r.content
        token = r.json()['access']
        client.credentials(
            HTTP_AUTHORIZATION=f'JWT {token}'
        )
        return token

    client.login = login

    yield client
