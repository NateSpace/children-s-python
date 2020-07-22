import turtle, math
s = turtle.Screen()
s.bgcolor("black")
t = turtle.Turtle()
t.shape("turtle")
t.color("#bada55") # can put in web color name, or hex value, or RGB value for color
t.speed(0) # 0 is the fastest speed (no animation), 1-10 are animated speeds with 1 being the slowest and 10 being the fastest 
t.pensize(3)
def square(size):
	for i in range(4):
		t.fd(size)
		t.rt(90)
def squares(size):
	while size > 0:
		square(size)
		t.penup()
		t.rt(45)
		t.fd(20/math.sqrt(2))
		t.lt(45)
		t.rt(5)
		t.pendown()
		size -= 20
def shape (sides, size):
  for i in range(sides):
    t.fd (size)
    t.rt(360.0/sides)
def shapes (sides, size, spacing):
  while size > 0:
    shape(sides, size)
    size -= spacing


def spiro(sides, size, steps, degrees):
	for i in range(360//degrees):
		shape(sides, size)
		t.fd(steps)
		t.rt(degrees)

spiro(sides = 5, size = 100, steps = 5, degrees = 18)