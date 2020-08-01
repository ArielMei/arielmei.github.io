# Use loops to draw a race track and create a racing turtle game.
# Each person pick a turtle and the one that gets the furthest is the winner.
# What you will learn
# Write for loops in Python; Use random numbers in Python; Draw lines in different colours with python Turtle
from turtle import *
from random import randint

t = Turtle()
t.speed(0)
t.penup()
t.goto(-200,140)
t.pencolor('grey')
t.fillcolor('purple')
# draw a race track
for step in range(10):  # returns six numbers, from 0 to 5
   t.write(step, align='center')      # write text to the screen
   t.right(90)        # makes the turtle turn right 90 degrees
   t.forward(10)  # draw a line
# # *-------- Option 1--------------------------
#    t.pendown()
#    t.forward(150)
# ## *------------Option 2----------------------
   for gap in range(10): # draw dash line
       t.pendown()
       t.forward(7.5)
       t.penup()
       t.forward(7.5)
## *----------------------------------
   t.penup()
   t.backward(160)
   t.left(90)
   t.forward(30)

t.penup()
# Add running turtle
ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-210,100)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-210,70)

for i in range(100):
#------------ Judge Winner ------------
    if ada.pos() >=(50,100):
        t.goto(0,180)
        t.pendown()
        t.write("Ada Wins!",font=("Arial", 16, "normal"))
        break
    elif bob.pos() >=(50,70):
        t.goto(0,180)
        t.pendown()
        t.write("Bob Wins!",font=("Arial", 16, "normal"))
        break
    else:
        ada.forward(randint(1,5))
        bob.forward(randint(1,5))
#------------ Code them moving ------------
#    ada.forward(randint(1,5))
#    bob.forward(randint(1,5))

t.hideturtle()
mainloop()
