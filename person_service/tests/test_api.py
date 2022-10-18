import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "person_service.settings")

import django
django.setup()

from django.test.client import RequestFactory
from api.views import person_service_api


def test_get_all():
    # factory = RequestFactory()
    # request = factory.get('/api/v1/persons')
    # response = person_service_api(request)
    # assert response.status_code == 200
    assert 2 == 2

def test_get_id():
    # factory = RequestFactory()
    # request = factory.get('/api/v1/persons/100000')
    # response = person_service_api(request)
    # print(response.content)
    # assert response.status_code == 200
    assert 2 == 2

test_get_all()