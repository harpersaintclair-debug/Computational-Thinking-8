import time
name1 = "Harper"

print(f"Hello there! i'm {name1}.")
time.sleep(1.3)
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
action = input("chose a action word ending in ing")
location1 = input("Now chose one more location like park or lake")
animal1 = input("now choose another animal")
emotion = input("Last but not least chose a emotion ")
name1 = input("I lied chose one more name")
    
print("Great ideas")
print("---------------------------------------------------------------------------------")
print(f"Once upon a time there was a {Animal}                                          ")
print(f"its name was {name}                                                            ")
print(f"And it lived by {location}                                                     ")
print(f"One day {name} was {action} by the {location1}                                 ")
print(f"They were feeling {emotion} when they saw a {animal1} walking down the street  ")
print(f"The {animal1} aproached and said hi my name is {name1}")
(f"Then {name} said hey you have a pretty cool {item1}")
print(f"The {animal1} said thank you {name1 } your also kinda cool")
print("---------------------------------------------------------------------------------")