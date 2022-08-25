import turtle as tl
size = 300
points = int(input('Enter the number of points of star : '))
angle = 180 - (180/points)
tl.bgcolor('black')
tl.pensize(2)
tl.speed('fastest')
for i in range(points):
	tl.color('red')
	tl.forward(size)
	tl.right(angle)
for i in range(points):
	tl.color('blue')
	tl.forward(size)
	tl.right(angle)
for i in range(points):
	tl.color('green')
	tl.forward(size)
	tl.right(angle)
for i in range(points):
	tl.color('orange')
	tl.forward(size)
	tl.right(angle)
