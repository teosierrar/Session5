#Virtual bartender
from random import choice

drinks=("vodka","wiskey","gin","tequila","rum","rakia","sake")
print("Welcome to the virtual pub")
name=input("I am the virtual bartender, how do I call you?")
try:
    age=input(f"How old are you, {name}?")
    age=int(age)
    if age>=21:
        Legal=True
    elif age<16:
        Legal=False
    else:
        print("Based on your age, I have to ask you where you are from")
        country=input(f"Where are you from, {name}?")
        Legal=False
        if age >= 21:
            legal=True
        elif age >=18 and country != "USA":
            Legal=True
        elif age >= 16 and country == "Luxembourg":
            Legal=True
    if Legal:
        print("You are allowed to drink")
        print(f"Here is a {choice(drinks)} for you")
    else:
        print(f"Dear {name}, I cannot serve you")
    if age>120 or age<5:
        print("Please do not lie to the virtual bartender")
except ValueError:
    print("Please enter a valid number")