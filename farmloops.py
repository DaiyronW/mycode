#!/usr/bin/python3

import html 
import random

farms = [
    {"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
    {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
    {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
    {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}
]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

#P1
for farm in farms:
    if farm["name"] == "Northeast Farm":
        print("Animals from Northeast Farm:")
        for animal in farm["agriculture"]:
            print(animal)
        print()

#P2
user_choice = input("Choose farm(Southwest Farm, Northeast Farm, East Farm, or West Farm): ")

for farm in farms:
    if farm["name"] == user_choice:
        print(f"the {user_choice} raises: {', '.join(farm['agriculture'])}")
        break
else:
    print("farm not found")

user_choice = input("choose a farm(Southwest Farm, Northeast Farm, East Farm, or West Farm")

for farm in farms:
    if farm["name"] == user_choice:
        farm_animals = [item for item in farm["agriculture"] if item in animals]
        if farm_animals:
            print(f"the {user_choice} raises the following animals: {','.join(farm_animals)}")
        else:
            print(f"the {user_choice} does not raise any animals.")
        break
else:
    print("farm not found.")
