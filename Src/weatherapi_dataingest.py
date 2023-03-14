import os
import datetime
from decimal import Decimal
from django.db import transaction
from api.models import Weather

# TODO : Define a function to ingest data
def ingest_data():
    data_dir = 'wx_data' # The directory where data files are stored

    # TODO : Loop through all files in the data directory
    for filename in os.listdir(data_dir):
        station_id = os.path.splitext(filename)[0]
        with open(os.path.join(data_dir, filename), 'r') as f:
            for line in f: # Loop through each line in the file
                line = line.strip() 
                if not line:
                    continue
                date_str, max_temp_str, min_temp_str, precipitation_str = line.split('\t')  # Split the line into four fields using tab as the delimiter
                date = datetime.datetime.strptime(date_str, '%Y%m%d').date()
                max_temperature = Decimal(max_temp_str) / Decimal('10')
                min_temperature = Decimal(min_temp_str) / Decimal('10')
                precipitation = Decimal(precipitation_str) / Decimal('10')

                # Skip any lines with missing data (-999.9)
                if max_temperature == -999.9 or min_temperature == -999.9 or precipitation == -999.9:
                    continue

                # Creating a new Weather object with the extracted data and save it to the database
                weather = Weather(date=date, station_id=station_id, max_temperature=max_temperature, min_temperature=min_temperature, precipitation=precipitation)
                weather.save()

if __name__ == '__main__':
    with transaction.atomic():
        Weather.objects.all().delete()
        ingest_data()
