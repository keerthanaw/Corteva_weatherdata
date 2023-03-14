'''
To ingest the weather data from the raw text files supplied into the database, we can follow these steps:

-Connect to the database using the credentials provided.
-For each weather data file, open the file and read each line.
-For each line, split the line into its four fields using the tab character as the delimiter.
-Check if the record already exists in the database by searching for a record with the same date and weather station ID.
-If the record does not exist, insert a new record into the database.
-Log the start and end times and the number of records ingested.

'''

#Implementation in python using Sqlite3 module

import sqlite3
import os
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('weather.db')
c = conn.cursor()

# Define the table schema
c.execute('''CREATE TABLE IF NOT EXISTS weather (
                station_id TEXT,
                date INTEGER,
                max_temp REAL,
                min_temp REAL,
                precipitation REAL,
                PRIMARY KEY (station_id, date)
            )''')

# Iterate over the weather data files
start_time = datetime.now()
for filename in os.listdir('wx_data'):
    if filename.endswith('.txt'):
        with open(os.path.join('wx_data', filename)) as f:
            # Iterate over the lines in the file
            for line in f:
                # Parse the fields from the line
                fields = line.strip().split('\t')
                station_id = filename[:-4]  # remove the .txt extension
                date = int(fields[0])
                max_temp = float(fields[1])/10  # convert to degrees Celsius
                min_temp = float(fields[2])/10
                precipitation = float(fields[3])/10  # convert to millimeters
                
                # Check if the record already exists
                c.execute('SELECT count(*) FROM weather WHERE station_id = ? AND date = ?', (station_id, date))
                if c.fetchone()[0] == 0:
                    # Insert the new record
                    c.execute('INSERT INTO weather VALUES (?, ?, ?, ?, ?)', (station_id, date, max_temp, min_temp, precipitation))

# Commit the changes to the database
conn.commit()

# Log the statistics
end_time = datetime.now()
num_records = c.execute('SELECT count(*) FROM weather').fetchone()[0]
print(f'Ingested {num_records} records in {(end_time-start_time).total_seconds()} seconds.')
