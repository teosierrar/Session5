name=input("What is your name")
print("hello",name)
age=input("How old are you?")
try:
    print(name,"you were born in",2024-int(age))
    #anotehr way to format print is via f-strings
    print(f"{name}, you were born in {2024-int(age)}")
    #division=int(age)/0
except ValueError:
    print("Age must be a valid number")
    print(f"the value that you typed was {age}")
except ZeroDivisionError:
        print("You can't divide by zero")
except: #all other types of exceptions!
    print("No idea what else can go wrong")
else: # in case no exception happened
    print("Thanks for being a good sport and not trying to crash the app")
finally:
    print("Thanks for playing")