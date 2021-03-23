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

headers = {"Authorization": "Bearer " + contents}
query = {'term':'food', 'location':city, 'limit': 50}
response = requests.get("https://api.yelp.com/v3/businesses/search", params=query, headers=headers)
# print(response.json())

x = response.json()
# y = json.loads(x)
places = x['businesses']

count = 0



for place in places:
  count += 1
  print(place['name'] + ' Is Closed: ' +str(place['is_closed' ]) + ' Rating: ' + str(place['rating']) +': ' + str(count))



# Store in database
