"""
Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance.
This program may require finding coordinates for the cities like latitude and longitude.
"""

import geocoder, json
from geopy import distance

# BING API key
BING_API_KEY = "ApZEeQXVfhqHAtbsb4lxyYcqQI-asspthJToNAhK-tbfsk6wIZWZ8eYwcFuQWl2P"

# Prompt user for 2 locations, calculate distance in km and print the result.
def main():
    prompt_1 = input("Enter first location: ")
    prompt_2 = input("Enter second location: ")
    prompt_3 = input("Choose miles or kilometers: ")
    distance = calculate_distance(prompt_1, prompt_2, prompt_3)
    print(f"Distance between {prompt_1} and {prompt_2}: {distance:.2f} {prompt_3}") 

# Calculates the distance between both locations, default in kms.
def calculate_distance(location_1, location_2, unit_of_distance="kilometers"):
    location_1_geo_info = _get_geo_info(location_1)
    location_2_geo_info = _get_geo_info(location_2)
    
    # Tuple containing latitude and longitude coordinates.
    coordinates_location_1 = _get_coordinates(location_1_geo_info)
    coordinates_location_2 = _get_coordinates(location_2_geo_info)
    
    # Calculate the distance in miles or kms.
    if unit_of_distance == "kilometers":
        calculated_distance = distance.distance(coordinates_location_1, coordinates_location_2).km
    if unit_of_distance == "miles":
        calculated_distance = distance.distance(coordinates_location_1, coordinates_location_2).miles
    return calculated_distance
    
# Use BING API to collect geo info about the location, stored in a dictionary.    
def _get_geo_info(location):
    geo_search_bing = geocoder.bing(location={location}, key=BING_API_KEY)
    geo_info = geo_search_bing.json
    return geo_info   

# Get lat and lng out of this dictionary.
def _get_coordinates(geo_info):
    latitude = geo_info["lat"]
    longitude = geo_info["lng"]
    return (latitude, longitude)
    

main()
    
    

    





