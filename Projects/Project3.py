import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -200
y1 = 200
x2 = -200
y2 = 100
x3 = -200
y3 = -100  
x4 = -200
y4 = -200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("moon")
t1 = create_sprite("LebronCavs",x1,y1)
t2 = create_sprite("LebronGoof (1)",x2,y2)
t3 = create_sprite("LebronLakers",x3,y3)
t4 = create_sprite("LebronYoung",x4,y4)


# # Section 3 - Racing
# t4 is likely to win due to the high random choice number either them or t3 are most likely though all can win but T1 
for i in range(30):
    x1 += 7
    x2 += 13
    x3 += random.randint(5,28)
    x4 += random.choice([8,10,15,120,1])

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("LeBron wins!")
elif x2 >= x3 and x2 >= x4:
    print("LeBron wins!")
elif x3 >= x4:
    print("LeBron wins!")
else:
     print("Young LeBron wins!")


turtle.exitonclick()