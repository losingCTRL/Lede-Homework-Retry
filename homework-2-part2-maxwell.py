print("Margaux Maxwell")
from datetime import date
print((date.today()))
print("Homework 2, Part 2")

#PART TWO: Lists

countries = ["Albania", "Colombia", "Sweden", "Mongolia", "Argentina", "Finland", "Norway"]
for country in countries:
  print(country)
countries.sort()
print(countries)
print(countries[0])
print(countries[-2])
countries.remove('Colombia')
print(countries)
uppercase = [country.upper() for country in countries]
print(uppercase)

#PART TWO: Dictionaries

tree = { 
    'name': 'Rumskulla oak', 
    'species': 'Common oak', 
    'age': 1000, 
    'location_name': 'Vimmerby, Sweden',
    'latitude': 57.669034, 
    'longitude': 15.858857, 
}

print("The", tree['name'], "is a", tree['age'], "year old tree", "that grows in", tree['location_name'])

NYC = {
    'latitude': 40.7128, 
    'longitude': -74.0059,
} 

if NYC['latitude']  == tree['latitude']:
    print("We are both at the same latitude")

if NYC['latitude']  > tree['latitude']: 
    print("The", tree['name'], "in", tree['location_name'], "is south of NYC")

if NYC['latitude']  < tree['latitude']:
    print("The", tree['name'], "in", tree['location_name'], "is north of NYC")
    
from datetime import date
import math
birth_day=input("Enter your day of birth: ")
birth_month=input("Enter your month of birth: ")
birth_year=input("Enter your year of birth: ")
birth_date = date.fromisoformat(birth_year+'-'+birth_month+'-'+birth_day)
print(birth_date)

today = date.today()
date_difference = today - birth_date
age = (math.floor(date_difference.days/365))
print(age)
print(tree['age'])

if age  == tree['age']:
    print("You are the same age as the Rumskulla oak")

if age  > tree['age']: 
    print("You are older than the Rumskulla oak")

if age  < tree['age']:
   print("You are younger than the Rumskulla oak")

#PART TWO: Lists of dictionaries

dictionarylist =[{'location_name': 'Moscow', 
            'latitude': 55.7558, 
            'longitude': 37.6173},
           {'location_name': 'Tehran', 
            'latitude': 35.7219, 
            'longitude': 51.3347},
            {'location_name': 'Falkland Islands', 
            'latitude': -51.7963, 
            'longitude': -59.5236},
            {'location_name': 'Seoul', 
            'latitude': 37.5519, 
            'longitude': 126.9918},
            {'location_name': 'Santiago', 
            'latitude': -33.4489, 
            'longitude': -70.6693},
            ]
for dictionary in dictionarylist:
    print(dictionary['location_name'])
    if dictionary['latitude'] > 0:
        print("Above the equator!")
    else:
        print("Below the equator!")
    if dictionary['location_name'] == 'Falkland Islands':
       print(f"The Falkland Islands are a biogeographical part of the mild Antarctic zone")
