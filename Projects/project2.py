import time
Kobe_points = 0
Lebron_points = 0
AE_points = 0   
Rodman_points = 0
Harden_points = 0
Shaq_points = 0
Jokic_points = 0
kyrie_points = 0
curry_points = 0
wemby_points = 0



print("WHO DO YOU PLAY LIKE")
time.sleep(1)
print("Answer some questions to find out(be honest)")
time.sleep(1)
print("All answers have to be CAPITOL letters with no spaces")
time.sleep(1)
print("Question 1:")
time.sleep(1)
answer1 = input("Whats your most consistent shot|A. Shooting Threes| |B. Mid ranges| |C. Layups| |D. Floater| |Answer Here|:  ")
if answer1 == "A" :
    curry_points += 3
    AE_points += 1
    Harden_points += 2
    kyrie_points += 1
    Lebron_points += 1 
    Kobe_points += 1
    wemby_points += 1
elif answer1 == "B":
    Kobe_points += 3
    Lebron_points += 2
    kyrie_points += 1
    Jokic_points += 1
    curry_points += 0.5
    AE_points += 1.5
elif answer1 == "C":
    Shaq_points += 2
    kyrie_points += 2
    Rodman_points += 1
    Kobe_points += 1.5
    Lebron_points += 1
    wemby_points += 2
    AE_points += 2
elif answer1 == "D":
    Jokic_points += 2
    kyrie_points += 1
    curry_points += 1
    Harden_points += 1
    AE_points += 1.5
print("QUESTION 2")
answer2 = input("Which Is your most consistent stat.|A. Rebounding| |B. Assists| |C. Blocks| |D. Steals| |Answer|   ")
if answer2 == "A":
    Rodman_points += 4
    Shaq_points += 2.5
    Jokic_points += 2.5
    Lebron_points += 1.5
    Kobe_points += 1
    wemby_points += 1
elif answer2 == "B":
    AE_points += 1
    Jokic_points += 2.5
    kyrie_points += 1.5
    curry_points += 1.5
    Lebron_points += 1.5
    wemby_points += 1
elif answer2 == "C":
    wemby_points += 3
    Lebron_points += 2
    Shaq_points += 2
    AE_points += 2
elif answer2 == "D":
    Kobe_points += 3
    AE_points += 2
    Lebron_points += 2.5
print("QUESTION 3")
answer3 = input("You about to play a game how do you warmup 1 day before? |A = Eating Healthy| |B = Workout| |C = Stretching| ")
if answer3 == "A" or answer3 == "a":
    Shaq_points += 1.5
    Harden_points += 2
elif answer3 == "B":
    Kobe_points += 3
    Lebron_points += 1
    Shaq_points +=1
elif answer3 == "C":
    Kobe_points += 1
    wemby_points += 2
    Lebron_points += 1
    AE_points += 1.5
    curry_points += 1
print("QUESTION 4")
answer4 = input("Most common plays you run |A. Pick and Roll| |B.Dribble Hand Offs| |C. Fast Breaks| |D Isolation| |ANSWER HERE>>>| ")
if answer4 == "A":
    Shaq_points += 2
    Harden_points += 1
    Jokic_points += 1
    AE_points += 1.5
elif answer4 == "B":
    curry_points += 2
    wemby_points += 1.5
    AE_points += 1
elif answer4 == "C":
    Lebron_points += 1.5
    AE_points += 2.5
elif answer4 == "D":
    Harden_points += 3
    Kobe_points += 2
    curry_points += 1
    wemby_points += 1
    Shaq_points += 1
print("QUESTION 5")
answer5 = input("Which is your most dominant physical aspect |A.jumping| |B.Stamina| |C.Stregth| |D.Agility|")
if answer4 == "A":
    Shaq_points += 1
    Rodman_points += 1.5
    Lebron_points += 3
    Kobe_points += 1
    AE_points += 4
    wemby_points += 1.5
elif answer4 == "B":
    curry_points += 2.5
    Kobe_points += 2.5
    AE_points += 2
    Lebron_points += 1.5
elif answer4 == "C":
    Lebron_points += 2
    Shaq_points += 3.5
    Rodman_points += 2.5
    Kobe_points += 1.5
    Jokic_points += 2
elif answer4 == "D":
    Kobe_points += 2.5
    curry_points += 2.5
    Lebron_points += 1.5
    AE_points += 2

print("Are you ready for your answer!!! ")
if Kobe_points >= Lebron_points and Kobe_points >= AE_points and Kobe_points >= Rodman_points and Kobe_points >= Harden_points and Kobe_points >= Shaq_points and Kobe_points >= Jokic_points and Kobe_points >= kyrie_points and Kobe_points >= wemby_points and Kobe_points >= curry_points:
    print("You play like Kobe Bryant")
elif Lebron_points >= AE_points and Lebron_points >= Rodman_points and Lebron_points >= Harden_points and Lebron_points >= Shaq_points and Lebron_points >= Jokic_points and Lebron_points >= kyrie_points and Lebron_points >= wemby_points and Lebron_points >= curry_points:
    print("You play like Lebron James")
elif AE_points >= Rodman_points and AE_points >= Harden_points and AE_points >= Shaq_points and AE_points >= Jokic_points and AE_points >= kyrie_points and AE_points >= wemby_points and AE_points >= curry_points:
    print("You play like Anthony Edwards")
elif Rodman_points >= Harden_points and Rodman_points >= Shaq_points and Rodman_points >= Jokic_points and Rodman_points >= kyrie_points and Rodman_points >= wemby_points and Rodman_points >= curry_points:
    print("You play like Dennis Rodman")
elif Harden_points >= Shaq_points and Harden_points >= Jokic_points and Harden_points >= kyrie_points and Harden_points >= wemby_points and Harden_points >= curry_points:
    print("You play like James Harden ")
elif Shaq_points >= Jokic_points and Shaq_points >= kyrie_points and Shaq_points >= wemby_points and Shaq_points >= curry_points:
    print("You play like Shaquile O'neal ")
elif Jokic_points >= kyrie_points and Jokic_points >= wemby_points and Jokic_points >= curry_points:
    print("You play like Nikola Jokic")
elif kyrie_points >= wemby_points and kyrie_points >= curry_points:
    print("You play like Kyrie Irving")
elif wemby_points >= curry_points:
    print("You play like Kyrie Irving")
else:
    print("You play like Steph Curry")
    
 

