from rest_framework.pagination import PageNumberPagination

#Create a Custom pagination class for weather data API
class WeatherDataPagination(PageNumberPagination):
    page_size = 10  # number of records per page
    page_size_query_param = 'page_size'  # override default page size query parameter
    max_page_size = 100  # maximum number of records per page
