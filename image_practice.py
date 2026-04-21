# Section 1 - Your code
from utils import *
set_background("lax")

s1 = create_sprite("basketball", 100, 100)
s2 = create_sprite("dog", -100, -100)
s2 = create_sprite("taco", -100, 100)
s2 = create_sprite("lebron(1)", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("pink")
message1.write("Hi Julia",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()