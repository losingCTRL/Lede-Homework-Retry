print("Margaux Maxwell")

print("Margaux Maxwell")

from datetime import date
import math

today = date.today()
print("Today's date:", today)

print("Homework 1")

birth_day=input("Enter your day of birth: ")
birth_month=input("Enter your month of birth: ")
birth_year=input("Enter your year of birth: ")
birth_date = date.fromisoformat(birth_year+'-'+birth_month+'-'+birth_day)
print(birth_date)

today = date.today()
date_difference = today - birth_date
age = math.floor(date_difference.days/365)
print (f"{math.floor(date_difference.days/365)} years")
print (f"{date_difference.days*80*60*24} human heartbeats")
print (f"{date_difference.days*30*60*24} blue whale heartbeats")
print (f"{date_difference.days*160*60*24} rabbit heartbeats")

print (f"{math.floor(date_difference.days/365)/0.615} Venus years")
print (f"{math.floor(date_difference.days/365)/165} Neptune years")

if age  == 29:
    print("We are twins!")

if age  > 29: 
    print("You are older and wiser")

if age  < 29:
    print("Almost caught up to me")