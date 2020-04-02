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


@pytest.fixture(scope='session')  # session, module, function  # autouse=True
def api_client():
    client = APIClient()  # LEGB

    def login(username, password):
        url_auth = reverse('token_obtain_pair')
        response = client.post(
            url_auth,
            data={'username': username, 'password': password},
            format='json',
        )
        assert response.status_code == 200
        access = response.json()['access']
        client.credentials(HTTP_AUTHORIZATION=f'JWT {access}')

    client.login = login

    yield client


@pytest.fixture(scope='session')
@pytest.mark.django_db
def user():
    from account.models import User
    # create user
    email = 'srjgkbdrgjdbr@mail.com'
    password = '1234567'
    initial_user = User.objects.create(email=email, username=email)
    initial_user.set_password(password)
    initial_user.save()

    initial_user.raw_password = password

    yield initial_user
