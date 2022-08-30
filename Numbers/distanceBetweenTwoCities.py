"""
Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance.
This program may require finding coordinates for the cities like latitude and longitude.
"""

import geocoder, json
from geopy import distance

# BING API key
BING_API_KEY = "ApZEeQXVfhqHAtbsb4lxyYcqQI-asspthJToNAhK-tbfsk6wIZWZ8eYwcFuQWl2P"

# prompt user for 2 locations
prompt_1 = input("Enter first location: ")
prompt_2 = input("Enter second location: ")

# use BING API to collect location info
location_1 = geocoder.bing(location={prompt_1}, key=BING_API_KEY)
location_2 = geocoder.bing(location={prompt_2}, key=BING_API_KEY)

# dictionary with info provided by BING services
results_1 = location_1.json
results_2 = location_2.json

# get lat and lng out of the dictionary
lat_location_1 = results_1["lat"]
lng_location_1 = results_1["lng"]
lat_location_2 = results_2["lat"]
lng_location_2 = results_2["lng"]
   
# calculate the distance in km's between both locations
coordinates_location_1 = (lat_location_1, lng_location_1)
coordinates_location_2 = (lat_location_2, lng_location_2)
distance = distance.distance(coordinates_location_1, coordinates_location_2).km
print(f"Distance between {prompt_1} and {prompt_2}: {distance:.2f} km") 
    
    

    
    

    





