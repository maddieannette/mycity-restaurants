import requests
import os
import json
import sqlite3
from sqlite3 import Error
from place import Place
import time
import datetime
import random

unix = int(time.time())
date = str(datetime.datetime.fromtimestamp(unix).strftime('''%Y-%m-%d %H:%M:%S'''))

# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.exectue()

db_file = os.getcwd() + "/data-retrieve-app/sqlite.db"
conn = sqlite3.connect('sqlite.db')
c = conn.cursor()

# Step One: Identify city to use 
city = 'Corpus Christi, Texas'
#Pull Api Key from ApiKeyFile
apiKeyPath = os.getcwd() + "/data-retrieve-app/apikey.txt"

myfile = open(apiKeyPath, "rt") # open lorem.txt for reading text
contents = myfile.read()         # read the entire file to string
myfile.close()                   # close the file
print(contents)

# Pull data for city - resturant from yelp

data_pull = 1

offset = 0
keep_going = True
call = 1
# review_count = 0



while data_pull <= 2 and keep_going:
    keep_going = False
    call += 1
    print('Data Pull:'+str(data_pull))
    headers = {"Authorization": "Bearer " + contents}
    params = {'term':'food', 'location':city, 'limit': 50, 'offset': offset, 'sort_by': 'review_count'}
    response = requests.get("https://api.yelp.com/v3/businesses/search", params=params, headers=headers)
    # print(response.json())

    responseData = response.json()
    places = responseData['businesses']    
    print(len(places))

    for place in places:
        keep_going = True
        offset += 1
        print(place['name']
        + ' Is Closed: '
        +str(place['is_closed' ])
        + ' Rating: '
        + str(place['rating'])
        + ' Review Count: '
        +  str(place['review_count'])
        + ' Longitude:'
        + str(place['coordinates']['longitude']) 
        + ' Latitude:'
        + str(place['coordinates']['latitude'] )
        + ' Offset: '
        + str(offset))
        c.execute('''INSERT INTO restaurants(name, rating, is_closed, review_count, longitude, latitude) VALUES(?, ?, ?, ?, ?, ?)''', (place['name'], place['rating'], place['is_closed'], place['review_count'], place['coordinates']['longitude'], place['coordinates']['latitude']))
    data_pull += 1


c.execute("SELECT * FROM restaurants")
print(c.fetchall())
conn.commit()
conn.close()
    
   
    




# db_file = os.getcwd() + "/data-retrieve-app/sqlite.db"
# conn = None
# try:
#     conn = sqlite3.connect(db_file)
#     print(sqlite3.version)
# except Error as e:
#     print(e)
# finally:
#     if conn:
#         conn.close()


print ('Execution finished')


