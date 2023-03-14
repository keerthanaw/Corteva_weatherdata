# Weather and Crop Yield Data Engineering Exercise
This project answers problems to the questions posed in Corteva_codechallenge 

## Data processing

The first initial three problems are based on Data Modeling, Ingestion and Analysis respectively
The Weather_data_processing folder has source code for the above tasks 

## Weather API 

This is a Django REST framework API that provides weather data for various weather stations in the Midwestern United States. The data is stored in the wx_data directory, with each file corresponding to a particular weather station. The API provides two endpoints for accessing weather data: /api/weather and /api/weather/stats.Each file in the wx_data directory contains weather data records for a particular weather station from Nebraska, Iowa, Illinois, Indiana, or Ohio.

Under src, weather_api is the project and api is the app

# Requirements

```
Python 3.6+
Django 3.2+
djangorestframework
drf-yasg (for Swagger documentation)
pytest (for unit tests)
```
# Set Up

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/weather-api.git
```

2. Install the required packages using pip:

```
pip install -r requirements.txt
```

3. Migrate the database:

```
python manage.py migrate
```

# Running the API

To run the API, simply run the following command:

```
python manage.py runserver
```

This will start the development server on http://localhost:8000.

# API Endpoints

# /api/weather
This endpoint returns weather data for the specified weather station(s) and date range. Clients can filter the data by specifying the station and/or date query parameters.

```
/api/weather?station=NE0001&date=19850101: Return data for station NE0001 on January 1, 1985
/api/weather?station__in=NE0001,NE0002&date__gte=19900101&date__lte=19901231: Return data for stations NE0001 and NE0002 between January 1, 1990 and December 31, 1990
```

# /api/weather/stats
This endpoint returns statistical summaries of weather data for the specified weather station(s) and date range. Clients can filter the data by specifying the station and/or date query parameters.

```
/api/weather/stats?station=NE0001&date=19850101: Return statistical summaries for station NE0001 on January 1, 1985
/api/weather/stats?station__in=NE0001,NE0002&date__gte=19900101&date__lte=19901231: Return statistical summaries for stations NE0001 and NE0002 between January 1, 1990 and December 31, 1990
```
# Pagination

Both endpoints support pagination using the page and page_size query parameters. Clients can specify the current page number using the page parameter (default is 1), and the page size using the page_size parameter (default is 10).

```
/api/weather?page=2&page_size=20: Return the second page of results with a page size of 20
```

# Swagger Documentation 

The API includes Swagger/OpenAPI documentation that provides an interactive interface for exploring and testing the API. This documentation can be accessed by navigating to http://localhost:8000/swagger/ in a web browser

# Running Tests 

To run the unit tests for the API, run the following command:

```
python manage.py test

```

# Linting

1. Install pylint by running the following command:

```
pip install pylint
```

2. Navigate to the root folder of your Django project in the terminal

3. Run the following command to check your project's code for linting errors:

```
pylint api
```
4. Code can be cleaned based on the lint score, which can be improved according to the suggestions by linting 
