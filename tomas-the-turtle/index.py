import turtle 
a = int(input("Angle size (integer):"))
c = int(input("Line length (integer):"))

spiral = turtle.Turtle()
spiral.shape('circle')
spiral.speed(10)
for i in range(10 ** 8):
    spiral.pendown()
    spiral.color('blue' if i % 2 == 0 else 'green')
    spiral.forward((i * 0.1) * c)
    spiral.right(a)
    spiral.dot()
    spiral.penup()
    
turtle.done()