import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -50
y1 = 100
x2 = -50
y2 = 200
x3 = -50
y3 = 10
x4 = -50
y4 = -150


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("flowers")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("balloon",x2,y2)
t3 = create_sprite("puppy",x3,y3)
t4 = create_sprite("can",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# #comment - The puppy will be the slowest and the balloon or the can will most likley be the winners because their random numbers start at 5 and end at a higher number therefore getting ahead of the puppy and the basketball.
for i in range(30):
    x1 += 5
    x2 += random.randint(5,12)
    x3 += 3
    x4 += random.randint(5,12)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.2)

s1 = create_sprite("bat", -100, 0)
# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s1.write("basketball wins!",font = ("Arial", 20, "normal"))
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s1.write("balloon wins!",font = ("Arial", 20, "normal"))
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    s1.write("puppy wins!",font = ("Arial", 20, "normal"))
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    s1.write("can wins!",font = ("Arial", 20, "normal"))
turtle.exitonclick()