## Create a dictionary of colours which maps hard to remember colour codes into fridendly names.
## What you will learn?
## 1. Dictionaries: creating and looking up values
## 2.Turtle graphics: text, fonts and colours
## Reminding the children that the comma ',' at the end of each dictionary entry

##----------- Start --------------

#from turtle import *
#
#screen = Screen()
#screen.setup(400,400)

##----------- Hex colour codes --------------
## jumpto.cc/colour-picker to choose colour which hex code beginning with a '#'

#screen.bgcolor('#A7E30E')
#
#color('#FA057F')
#style = ('Arial',40,'bold') # 40 is the font size
#write('Hello', font = style, align = 'center')
#hideturtle()

## ----------- Colour Dictionary -----------------
## A dictionary allows you to look up a value for any 'key' in the dictionary.
## A dictionary is contained in curly brackets.
## A colon : separates the key from the value. Comma, used to separate each key:value pair in the dictionary.

#colours = {
#    'verylime':'#A7E30E',
#    'reallyraspberry':'#FA057F',
#    'awesomeorange':'#F2A007'
#}
#
#print(colours['verylime'])
#print(colours['reallyraspberry'])
#
#screen.bgcolor(colours['verylime'])
#
### -------- Turtle ----------
#penup()
#goto(0,100)
#color(colours['reallyraspberry'])
#style = ('Arial',40,'bold') # 40 is the font size
#write('Hello', font = style, align = 'center')
#
#right(90)
#forward(60)
#color(colours['awesomeorange'])
#write('World', font = style, align = 'center')
#hideturtle()

## -------- Create a poster Using your own colour palette ---------
import turtle

style = ('Arial',40,'bold') # 40 is the font size

Colour = {
    'lightblue':'#94E8E9',
    'blue':'#2A07F2',
    'green':'#04D627',
    'red':'#D62704',
    'purple':'#AC04D6',
    'yellow':'#FDF910',
    'lightgreen':'#B5FBE5',
}
showList = ['A typical','smart phone','has more','computing power']

turtle.penup()
turtle.goto(0,0)
turtle.color(Colour['lightgreen'])
turtle.dot(350)  # draw a filled in circle with diameter 250

turtle.goto(0,-150)
for i in range(len(showList)):

    turtle.color(list(Colour.keys())[i])
    turtle.write(showList[i], font = style, align = 'center')
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)

turtle.hideturtle()

turtle.mainloop()
