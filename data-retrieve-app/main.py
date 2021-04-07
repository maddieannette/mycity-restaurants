import requests
import os
import json
import sqlite3
from sqlite3 import Error
from place import Place



p = Place()
p.name = 'BKK'
print(p.name)

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
results_list = []

while data_pull <= 2:
    print('Data Pull:'+str(data_pull))
    headers = {"Authorization": "Bearer " + contents}
    params = {'term':'food', 'location':city, 'limit': 50, 'offset': offset}
    response = requests.get("https://api.yelp.com/v3/businesses/search", params=params, headers=headers)
    # print(response.json())

    responseData = response.json()
    places = responseData['businesses']    

    for place in places:
        results_list.append(place['name'])
        results_list.append(place['rating'])
        # results_list.append(place['numOfReviews'])
        # results_list.append(place['longitude'])
        # results_list.append(place['latitude'])
        offset += 1
        print(place['name'] + ' Is Closed: ' +str(place['is_closed' ]) + ' Rating: ' + str(place['rating']) +': ' + str(offset))
        print(results_list)
        
    
    
    data_pull += 1




db_file = os.getcwd() + "/data-retrieve-app/sqlite.db"
conn = None
try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()


print ('Execution finished')



# # Python3 code here creating class
# class geeks: 
#     def __init__(self, name, roll): 
#         self.name = name 
#         self.roll = roll
   
# # creating list       
# list = [] 
  
# # appending instances to list 
# list.append( geeks('Akash', 2) )
# list.append( geeks('Deependra', 40) )
# list.append( geeks('Reaper', 44) )
  
# for obj in list:
#     print( obj.name, obj.roll, sep =' ' )
  
# # We can also access instances attributes
# # as list[0].name, list[0].roll and so on.