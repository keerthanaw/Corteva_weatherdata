from datetime import date
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Weather
from .serializers import WeatherSerializer
from rest_framework.test import APITestCase


# TODO: Create a test suite for Weather API views and endpoints
class WeatherAPITest(TestCase):

    def setUp(self):
        """
        Creating instances of Weather model for testing
        """
        self.client = APIClient()
        self.weather1 = Weather.objects.create(
            date=date(2022, 1, 1),
            station_id='NE001',
            max_temperature=Decimal('5.6'),
            min_temperature=Decimal('-2.3'),
            precipitation=Decimal('3.5')
        )
        self.weather2 = Weather.objects.create(
            date=date(2022, 1, 2),
            station_id='NE001',
            max_temperature=Decimal('4.4'),
            min_temperature=Decimal('-1.7'),
            precipitation=Decimal('0.0')
        )

    def test_list_weather(self):
        """
        Test listing all weather data
        """
        url = reverse('weather-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        expected_data = WeatherSerializer([self.weather1, self.weather2], many=True).data
        self.assertEqual(response.json(), expected_data)

    def test_filter_weather_by_date(self):
        """
        Test filtering weather data by date
        """
        url = reverse('weather-list')
        response = self.client.get(url, {'date__gte': '2022-01-02'})
        self.assertEqual(response.status_code, 200)
        expected_data = WeatherSerializer([self.weather2], many=True).data
        self.assertEqual(response.json(), expected_data)

    def test_filter_weather_by_station_id(self):
        """
        Test filtering weather data by station ID
        """
        url = reverse('weather-list')
        response = self.client.get(url, {'station_id': 'NE001'})
        self.assertEqual(response.status_code, 200)
        expected_data = WeatherSerializer([self.weather1, self.weather2], many=True).data
        self.assertEqual(response.json(), expected_data)

    def test_get_weather_stats(self):
        """
        Test getting weather statistics
        """
        url = reverse('weather-stats')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        expected_data = {
            'max_temperature': {
                'NE001': {
                    'value': '5.6',
                    'date': '2022-01-01'
                }
            },
            'min_temperature': {
                'NE001': {
                    'value': '-2.3',
                    'date': '2022-01-01'
                }
            },
            'precipitation': {
                'NE001': {
                    'value': '3.5',
                    'date': '2022-01-01'
                }
            }
        }
        self.assertEqual(response.json(), expected_data)


class WeatherViewSetTestCase(APITestCase):
    
    def test_paginated_response(self):
        # create some sample data
        weather_data = [{'date': '19850101', 'max_temp': 100, 'min_temp': 50, 'precipitation': 10},
                        {'date': '19850102', 'max_temp': 90, 'min_temp': 40, 'precipitation': 5},
                        {'date': '19850103', 'max_temp': 80, 'min_temp': 30, 'precipitation': 0},
                        {'date': '19850104', 'max_temp': 70, 'min_temp': 20, 'precipitation': -9999},
                        {'date': '19850105', 'max_temp': 60, 'min_temp': 10, 'precipitation': -9999},
                        {'date': '19850106', 'max_temp': 50, 'min_temp': 0, 'precipitation': -9999}]
        
        # create Weather objects from weather_data
        for weather in weather_data:
            Weather.objects.create(date=weather['date'],
                                    max_temp=weather['max_temp'],
                                    min_temp=weather['min_temp'],
                                    precipitation=weather['precipitation'])
        
        # test pagination
        response = self.client.get('/api/weather?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 3)
        
        # test that results are ordered by date
        response = self.client.get('/api/weather?ordering=date')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['date'], '19850101')
        self.assertEqual(response.data['results'][5]['date'], '19850106')

