import turtle
turtle.shape('turtle')
finn=turtle.clone()
finn.shape('square')
finn.goto(100,0)
finn.goto(100,100)
finn.goto(0,100)
finn.goto(0,0)
charlie=turtle.clone()
charlie.penup()
charlie.goto(200,0)
charlie.pendown()
charlie.goto(400,0)
charlie.goto(300,100)
charlie.goto(200,0)
finn.goto(300,300)
finn.stamp()
finn.goto(100,300)
turtle.clearstamps()
turtle.mainloop()

