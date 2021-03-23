import requests
import os
import json
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

while data_pull <= 2:
    print('Data Pull:'+str(data_pull))
    headers = {"Authorization": "Bearer " + contents}
    params = {'term':'food', 'location':city, 'limit': 50, 'offset': offset}
    response = requests.get("https://api.yelp.com/v3/businesses/search", params=params, headers=headers)
    # print(response.json())

    responseData = response.json()
    places = responseData['businesses']    

    for place in places:
        offset += 1
        print(place['name'] + ' Is Closed: ' +str(place['is_closed' ]) + ' Rating: ' + str(place['rating']) +': ' + str(offset))

    
    
    data_pull += 1
print ('Execution finished')
