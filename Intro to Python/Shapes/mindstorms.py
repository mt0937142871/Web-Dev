import turtle 
import time

def draw_square():
	square = turtle.Turtle()
	square.shape("turtle")
	square.color("white")
	square.speed(100)

	for i in range(0, 36):
		if i%6 == 0:
			square.fill(True)
		for j in range(0, 4):
			square.forward(150)
			square.right(90)
		square.fill(False)
		square.right(10)


def draw_circle():
	circle = turtle.Turtle()
	circle.shape("circle")
	circle.color("yellow")
	circle.speed(100)


	for i in range(0, 24):
		circle.circle(50)
		circle.right(15)

def draw_triangle():
	triangle = turtle.Turtle()
	triangle.shape("triangle")
	triangle.color("blue")
	triangle.speed(100)

	for i in range(0, 18):
		for j in range(0, 3):
			triangle.forward(250)
			triangle.right(120)
		triangle.right(20)

def draw_flower():
	polygon = turtle.Turtle()
	polygon.shape("turtle")
	polygon.color("green")
	polygon.speed(100)

	for i in range(0, 48):
		for j in range(0, 4):
			polygon.forward(150)
			polygon.right(45 + (j%2)*90)
		polygon.right(7.5)

def main():
	window = turtle.Screen()
	window.bgcolor("red")

	draw_flower()

	window.exitonclick()

if __name__ == "__main__":
 	main()
