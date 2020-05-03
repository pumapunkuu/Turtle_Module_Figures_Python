import turtle
def make_window(colr,ttle):
    w=turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w
def make_turtle(colr,sz):
    t=turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t
i=0.0
def move():
    tess.forward(-100)
    tess.left(90)
    a=0.0
    for i in range(16):
        if(a==0):
            tess.right(90+a)
            tess.forward(100)
            tess.right(90)
            tess.forward(100)
            tess.right(90)
            tess.forward(100)
            tess.right(90)
            tess.forward(100)
            tess.right(90)
            tess.forward(100)
            a=a+22.5
        else:
            tess.right(90+a)
            tess.forward(100)
            tess.right(90)
            tess.forward(100)
            tess.right(90)
            tess.forward(100)
            tess.right(90)
            tess.forward(100)
            a=a+22.5
wn=make_window('black','Dancing')
tess=make_turtle('purple',5)
move()
tess.color('white')
tess.showturtle()
wn.mainloop()