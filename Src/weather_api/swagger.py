from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path

# Defining a schema view using the get_schema_view function
schema_view = get_schema_view(
    # Defining the openapi.Info object with various attributes
    openapi.Info(
        title="Weather API",
        default_version='v1',
        description="API for weather data from 1985-01-01 to 2014-12-31",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@weatherapi.local"),
        license=openapi.License(name="MIT License"),
    ),
    # Set the "public" attribute to True, meaning anyone can access the API
    public=True,
    # Set the "permission_classes" attribute to an empty list, meaning no authentication is required to access the API
    permission_classes=[],
)

# Define the urlpatterns for the Django project
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
