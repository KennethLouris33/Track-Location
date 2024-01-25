import phonenumbers
import time
from phonenumbers import carrier
from phonenumbers import geocoder
# import opencage
from opencage.geocoder import OpenCageGeocode
import folium

# Gets user input
name = input("What is your name?")
num = input("Starting with its country code, what is your phone number?")


var1 = phonenumbers.parse(num) 
var2 = phonenumbers.parse(num)
location = geocoder.description_for_number(var2, "en")
carrier = carrier.name_for_number(var1, "en")

key = '9a53be6735d24fb5a11e6de8bf0bec89'
geocoder = OpenCageGeocode(key)
query = str(location)

results = geocoder.geocode(query)

# print(results)
lat = results[0]["geometry"]['lat']
lng = results[0]['geometry']['lng']
print(name + " your phone number " + num + " is a " + carrier + " Telecommunication currently located in " + location) 
print("Here is the coordinates: ", lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
time.sleep(60)

