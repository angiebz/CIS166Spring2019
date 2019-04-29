## Angelique Sanchez
## Project 2
## April 27, 2019


from graphics import *
'''
conversion code below
'''
def poundsconvert():
    grams = round(number * 452.592,2)
    kilograms = round(number / 0.453592,2)
    ounces = number * 16

    gramsbox.setText(grams)
    kbox.setText(kilograms)
    ozbox.setText(ounces)
    
win = GraphWin("Converter", 600, 350)
win.setBackground("purple")

instructions=Text(Point(280,20),"Weight Converter: Please enter a number and click convert")
instructions.draw(win)

poundstext = Text(Point(160, 50), "Pounds:")
poundstext.draw(win)
'''
Entry box for the user to input the number of pounds that will be converted
'''
poundsbox = Entry(Point(win.getWidth() / 2, 50), 25)
poundsbox.setFill("White")
poundsbox.draw(win)

gramstext = Text(Point(160, 100), "Grams:")
gramstext.draw(win)

gramsbox1= Rectangle(Point(205,90),Point(395,110))
gramsbox1.setFill("white")
gramsbox1.draw(win)

gramsbox = Text(Point(win.getWidth() / 2, 100), "")
gramsbox.setTextColor("black")
gramsbox.draw(win)

ktext = Text(Point(160, 150), "Kilograms:")
ktext.draw(win)

kbox1= Rectangle(Point(205,140),Point(395,160))
kbox1.setFill("white")
kbox1.draw(win)

kbox = Text(Point(win.getWidth() / 2, 150), "")
kbox.draw(win)

oztext = Text(Point(160, 200), "Ounces:")
oztext.draw(win)

ozbox1= Rectangle(Point(205,190),Point(395,210))
ozbox1.setFill("white")
ozbox1.draw(win)

ozbox = Text(Point(win.getWidth() / 2, 200), "")
ozbox.draw(win)

button1= Rectangle(Point(142,290),Point(206,310))
button1.setOutline("black")
button1.setFill("white")
button1.draw(win)

button= Text(Point(win.getWidth()/3.5,300),"Convert")
button.setOutline("black")
button.draw(win)
'''
buttons below for the user to click convert or close to exit the window
'''
        
closebutton= Rectangle(Point(362, 290),Point(438,310))
closebutton.setOutline("black")
closebutton.setFill("white")
closebutton.draw(win)

closebutton1 = Text(Point(win.getWidth() / 1.5, 300), "Close")
closebutton1.setOutline("black")
closebutton1.draw(win)

'''
while loop to prompt the user to enter a valid number if they enter invalid input
and calling the function to convert the number of pounds entered.
'''
while True:
    win.getMouse()
    instructions.setText("Please enter a number")

    try:
        number = int(poundsbox.getText())
        poundsconvert()
        
        p= win.getMouse()
        if p.getX() >= 362 and p.getX() <= 438:
            if p.getY () >= 290 and p.getY() <= 438:
                win.close()


    except ValueError:
        instructions.setText("Invalid input, Please enter a number")
        
