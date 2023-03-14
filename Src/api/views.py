"""
Views for the project are configured here
"""

from django.db.models import Avg, Max, Min
from rest_framework import filters, viewsets, views
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Weather
from .pagination import WeatherDataPagination
from .serializers import WeatherSerializer


class WeatherViewSet(viewsets.ModelViewSet):
    """
    Class WeatherViewSet for data view from weather model
    """

    # Set queryset for the viewset to fetch data from Weather model
    queryset = Weather.objects.all()
    # Set serializer class to serialize/deserialize Weather data
    serializer_class = WeatherSerializer
    # Set pagination class for the viewset
    pagination_class = WeatherDataPagination

    # Set fields on which filtering can be applied
    filterset_fields = ['date', 'station_id']
    # Set filter backends for the viewset
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    # Set fields on which ordering can be applied
    ordering_fields = ['date', 'max_temperature', 'min_temperature', 'precipitation']

    def list(self):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class WeatherStatsView(views.APIView):
    """
    Class created for weather data statistics
    """

    serializer_class = WeatherSerializer
    # Set pagination class for the view
    pagination_class = WeatherDataPagination

    # Define a method called get that accepts a request parameter
    def get(self, request):
        # Query the Weather model and calculate various statistics using the aggregate function
        stats = Weather.objects.aggregate(
            avg_max_temperature=Avg('max_temperature'),
            avg_min_temperature=Avg('min_temperature'),
            avg_precipitation=Avg('precipitation'),
            max_max_temperature=Max('max_temperature'),
            min_min_temperature=Min('min_temperature'),
            max_precipitation=Max('precipitation'),
        )
        return Response(stats)

    def get_queryset(self):
        queryset = Weather.objects.all()
        station_id = self.request.query_params.get('station_id', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if station_id is not None:
            queryset = queryset.filter(station_id=station_id)
        if start_date is not None:
            queryset = queryset.filter(date__gte=start_date)
        if end_date is not None:
            queryset = queryset.filter(date__lte=end_date)

        return queryset
