from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .views import  BaseModelViewSet
from .models import Aircraft, Flight
from .serializers import AircraftSerializer, FlightSerializer


class BaseModelViewSetTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Setup initial data for the tests
        cls.aircraft = Aircraft.objects.create(
            user_id=1,
            guid='00000000-0000-0000-0000-000000000001',
            platform=1,
            _modified=1616317613,
            meta={'field1': 'value1', 'field2': 'value2'}
        )
        cls.flight = Flight.objects.create(
            user_id=1,
            guid='00000000-0000-0000-0000-000000000002',
            platform=2,
            _modified=1616317613,
            meta={'fieldA': 'valueA', 'fieldB': 'valueB'}
        )

    def test_get_serializer_class(self):
        # Test that the correct serializer is returned based on the model
        viewset = BaseModelViewSet()
        viewset.kwargs = {'table_name': 'aircraft'}
        self.assertEqual(viewset.get_serializer_class(), AircraftSerializer)

        viewset.kwargs = {'table_name': 'flight'}
        self.assertEqual(viewset.get_serializer_class(), FlightSerializer)

    def test_get_queryset(self):
        # Test that the correct queryset is returned based on the model
        viewset = BaseModelViewSet()
        viewset.kwargs = {'table_name': 'aircraft'}
        queryset = viewset.get_queryset()
        self.assertEqual(list(queryset), [self.aircraft])

        viewset.kwargs = {'table_name': 'flight'}
        queryset = viewset.get_queryset()
        self.assertEqual(list(queryset), [self.flight])

    def test_bulk_create(self):
        # Test the bulk_create action
        url = reverse('base-list', kwargs={'table_name': 'aircraft'})
        data = {
            'table_name': 'aircraft',
            'items': [
                {'user_id':1,'guid': '00000000-0000-0000-0000-000000000003', 'platform': 3, '_modified': 1616317613,
                 'meta': {'field3': 'value3'}},
                {'user_id': 1, 'guid': '00000000-0000-0000-0000-000000000003', 'platform': 3, '_modified': 1616317613,
                 'meta': {'field3': 'value3'}},
            ]
        }
        response = self.client.post(url + 'bulk_create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Aircraft.objects.count(), 3)

    def test_search(self):
        url = reverse('base-list', kwargs={'table_name': 'aircraft'})
        response = self.client.get(url + 'search/', {'search': 'value1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['guid'], self.aircraft.guid)

        response = self.client.get(url + 'search/', {'search': 'nonexistent'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
