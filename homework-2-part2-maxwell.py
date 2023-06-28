
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
    'age': '1000', 
    'location_name': 'Vimmerby, Sweden',
    'latitude': '57.669034N', 
    'longitude': '15.858857E', 
}

print("The", tree['name'], "is a", tree['age'], "year old tree", "that grows in", tree['location_name'])

NYC = {
    'latitude': '40.7128N', 
    'longitude': '-74.0059W',
} 

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
age = ({math.floor(date_difference.days/365)})
print (f"{math.floor(date_difference.days/365)} years old")

if 'age'  == tree['age']:
    print("You are the same age as the Rumskulla oak")

if 'age'  > tree['age']: 
    print("You are older than the Rumskulla oak")

if 'age'  < tree['age']:
   print("You are younger than the Rumskulla oak")