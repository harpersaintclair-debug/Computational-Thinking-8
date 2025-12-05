import time


print("Hello there!")
Answer = input("Do you want to help me build a story yes/no ")
if (Answer=="yes"): 
    print("Great lets do it")
else:
    print("Well its not like you have a choice")
    time.sleep(1.5)
    Animal = input("Chose a animal.")
    print("Good choice!!")
    location = input("Chose a place")
    name = input("Choose a name")
    item1 = input("Chose a item")
    print("Great ideas")

    print(f"Once upon a time there was a {Animal}")
    print(f"its name was {name}")
    print(f"and it lived in {location}")
    
