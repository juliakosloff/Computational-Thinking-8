from utils import *
import random
import time

# Section 1 - setup

set_background("park")
x1 = -50
y1 = 100
x2 = -50
y2 = 200
x3 = -50
y3 = 10
x4 = -50
y4 = -150

t1 = create_sprite("puppy",x1,y1)
t2 = create_sprite("dog",x2,y2)

money = 2
puppy = 1
dog = 0


m1 = create_sprite("alien", -200,200)
m1.hideturtle()




# Section 2 - controls
# get_puppy gives you a puppy at a random point on the screen when you press the space key.
def get_puppy():
    global puppy
    puppy += 1
    x = random.randint (-200,200)
    y= random.randint (-200,200)
    create_sprite("puppy",x,y)
window.onkeypress(get_puppy,"space")



# get_dog gives you a dog at the bottom of the screen and adds one more dog variable to the top of the screen and this happens when you have 3 or more puppies and your money is greater than two (more puppies=more money) it also changes the money variable at the top of the screen.  
def get_dog(): 
    global dog, puppy, money
    if puppy >= 3 and money >= 10: 
        puppy -= 3
        money -= 10                 
        dog += 1

        x = -400 + 120 * dog
        y = -250
        create_sprite("dog", x, y)
        
window.onkeypress(get_dog,"f")







# Section 3 - game loop
window.listen()
for i in range(1000000):

    if i % 200 == 0:
        money += puppy * 0.03
        money += dog * 0.005

    m1.clear()
    m1.write(f"Puppies: {puppy}\nDogs: {dog}\nMoney: {int(money)}", font=("Arial",30,"normal"))

    time.sleep(0.01)
    window.update()
    # The goal of my game is to get the most dogs with the money you have that you get from the puppies so more puppies can get you more dogs.