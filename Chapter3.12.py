import turtle
wn=turtle.Screen()
wn.bgcolor('lightgreen')
wn.title("Turtle-i Zina")
alex=turtle.Turtle()
alex.shape('turtle')
alex.color('blue')

aim=30
alex.penup()
alex.stamp()
alex.forward(100)
for i in range(12):
    alex.stamp()
    alex.right(180)
    alex.forward(100)
    alex.right(180+aim)
    alex.forward(100)
        
    
    
wn.mainloop()


