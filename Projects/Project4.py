import turtle, time, random
from utils import *

# Section 1 - setup
set_background("Kitchen")
Cookie_dude = create_sprite("Cookie1", 0 -120)
Grams = create_sprite("Sleepy_gma",220,24)
# TODO - create at least two variables and set their starting value. ex: cookies = 0
Cookie = 0
Grandmas_level = 0
Money = 0
Money_Making = 1
Cookie_making = 0
Cookie_PC = 1


# OPTIONAL: use this invisible alien to say a message
message_sprite1 = create_sprite("alien", -315,235)
message_sprite1.hideturtle()
message_sprite1.write(f"Cookies: {Cookie}", font = ("Arial", 25,"normal"))

# Sprite two
message_sprite2 = create_sprite("bat", -315,180)
message_sprite2.hideturtle()
message_sprite2.write(f"Money: {Money}", font = ("Arial", 25,"normal"))

# Sprite 3
message_sprite3 = create_sprite("bench", 120,235)
message_sprite3.hideturtle()
message_sprite3.write(f"Grandma: {Grandmas_level}", font = ("Arial", 25,"normal"))

# How to play in terminal
print("How To Play MY Cookie Clicker Game:")
input()
print("The Goal Is To Get As Many Cookies As Possible Try To Reach 1 Million")
input()
print("Press The Space Key To Get A Cookie Make Sure You Have 5 Dollars Though ")
input()
input()
print("Grandmas Get You More Money And A Cookie Every Once In A While ")
input()
print("You Can Upgrade Them As Much As You Want")
input()
print("You Can Also Increase How Many Cookies You Get Per Second With The A Key")
input()
print("That Will Be All Now Get To Playing")


# Section 2 - controls
# With Space Key Get A Cookie
def get_cookie ():
    global Cookie, Money, Cookie_PC
    if Money >= Cookie_PC * 5:
        # Cookie += 1
        Cookie += Cookie_PC
        Money -= 5 * Cookie_PC 
        set_image(Cookie_dude, "Cookie2")
       
    


window.onkeypress(get_cookie, "space")
# Control 2
# With W Key Get Or Upgrade Grandma To Make Money And An Occansional Couple Cookies
def get_grandma ():
    global Grandmas_level, Money, Money_Making, Cookie, Cookie_making
    if Cookie >= 5:
        Grandmas_level += 1
        Cookie -= 5
        Money_Making += 3
        Cookie_making += 1
        set_image(Grams, "Awake_gma")
window.onkeypress(get_grandma,"w")
   




# Control three
# With The S Key Upgrade Cookies Per Click
def CPC ():
    global Cookie, Money, Cookie_PC
    if Money >= 5* Cookie_PC:
       
        # Cookie += Cookie_PC
        # Money -= 5 * Cookie_PC 
        Cookie_PC += 1
        
       
    


window.onkeypress(CPC, "s")

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite1.clear()
    message_sprite1.write(f"Cookies: {Cookie}", font = ("Arial", 25,"normal"))

    # Sprite two
    message_sprite2.clear()
    message_sprite2.write(f"Money: {Money}", font = ("Arial", 25,"normal"))

    # Sprite 3
    message_sprite3.clear()
    message_sprite3.write(f"Grandma: {Grandmas_level}", font = ("Arial", 25,"normal"))
    if i % 75 == 0:
        Money += Money_Making

    if i % 500 == 0:
        Cookie += Cookie_making
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")
    if i % 40 == 0:
        set_image(Cookie_dude, "Cookie1")
    time.sleep(0.01)
    window.update()








