france_points = 0
usa_points = 0
mexico_points = 0
greece_points = 0

print(" Today we are going ot see where you are going to live when you grow up!")
input()
answer1 = input(" Do you prefer eating A baguettes, B hot dogs, C tacos, or D gyros? ")
if answer1 == "A":
    france_points += 1
elif answer1 == "B":
    usa_points += 1
elif answer1 == "C":
    mexico_points += 1
elif answer1 == "D":
    greece_points += 1
input()
answer2 = input(" Would you rather be fluent in A french, B english, C spanish, or D greek? ")
if answer2 == "A":
    france_points += 1
elif answer2 == "B":
    usa_points += 1
elif answer2 == "C":
    mexico_points += 1
elif answer2 == "D":
    greece_points += 1
input()
answer3 = input(" Do you prefer wearing A heals, B slides, C flip flops, or D sneakers? ")
if answer3 == "A":
    france_points += 1
elif answer3 == "B":
    usa_points += 1
elif answer3 == "C":
    mexico_points += 1
elif answer3 == "D":
    greece_points += 1
input()
answer4 = input (" Would you rather drink A orange soda, B water, C jarritos, or D coke? ")
if answer4 == "A":
    france_points += 1
elif answer4 == "B":
    usa_points += 1
elif answer4 == "C":
    mexico_points += 1
elif answer4 == "D":
    greece_points += 1
input()
answer5 = input(" What animal would you rather have a A Cat, B One dog and one cat, C Dog, or D goat? ")
if answer5 == "A" or answer5 == "a":
    france_points += 1
elif answer5 == "B":
    usa_points += 1
elif answer5 == "C":
    mexico_points += 1
elif answer5 == "D":
    greece_points += 1




print(f"Your score is {france_points} france, {usa_points} usa,{mexico_points} mexico, and {greece_points} greece")
input()
# End: determine results
if france_points >= usa_points and france_points >= mexico_points and france_points >= greece_points:
    print(" You are going to live in France!")
elif usa_points >= france_points and usa_points >= mexico_points and usa_points >= greece_points:
    print(" You are going to live in the usa!")
elif mexico_points >= france_points and mexico_points >= usa_points and mexico_points >= greece_points:
    print(" You are going to live in mexico!")
elif greece_points >= france_points and greece_points >= usa_points and greece_points >= mexico_points:
    print(" You are going to live in Greece!")
