# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("moon")

s1 = create_sprite("JEFF (1)", -100, 0)
s2 = create_sprite("Jacob", 100, 0)

s1.color("pink")
s2.color("dark red")
time.sleep(5)

s1.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(2)

s1.clear()
window.update()
time.sleep(2)

s2.write("On the moon!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(2)

s2.clear()
window.update()
time.sleep(2)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s1.write("Have you seen them?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.write("no",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
s1.write("Then lets go find them!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s2.write("I want to learn spanish tho",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
s1.write("Too bad",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s2.write("VAMOSSSSSS!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
s1.write("HMMM I dont see them anywhere...",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s2.write("I guess we have to go back.",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()
