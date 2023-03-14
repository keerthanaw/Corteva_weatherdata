from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# TODO : Create a schema view for the API using drf_yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Weather API",  # Title of the API
        default_version='v1',  # Default version of the API
        description="API for weather data from Nebraska, Iowa, Illinois, Indiana, and Ohio",  # Description of the API
    ),
    public=True,  # Make the API viewable to the public
    permission_classes=[permissions.AllowAny],  # Allow any user to access the API
)

# TODO : Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('api/', include('api.urls')),  # URL for the API endpoints
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # URL for the API documentation using Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # URL for the API documentation using ReDoc
]
