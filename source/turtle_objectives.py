from turtle import Turtle, title, exitonclick, resetscreen
from typing import List
import random

def main():
    while True:
        try:
            print("Pentagon, square, circle or triangle".title())
            print("to exit the program [quit, exit or q]".title())
            shapes = ["pentagon", "square", "circle", "triangle"]
            quitting = ["quit", "exit", "q"]
            choice = input("draw shape: ".title()).strip().lower()
            
            if choice in quitting:
                print("exiting..".upper())
                break
            
            # chick the user input
            if choice not in shapes:
                raise ValueError("please select from the given shapes".upper())
            resetscreen
            if choice == "pentagon":
                pentagon = Turtle()
                colors = ["#030637", "#3C0753", "#720455", "#910A67", "#49108B"]
                hollow_pentagon(turtle=pentagon, colors=colors)
                
            elif choice == "square":
                squ_number = int(input("enter number of squares: ").strip())
                
                if not isinstance(squ_number, int) and squ_number > 0:
                    raise ValueError("must be positive number")
                
                square = Turtle()
                colors = ["#0F0F0F", "#232D3F", "#005B41", "#008170","#04364A",
                            "#176B87", "#64CCC5", "#DAFFFB", "#C5E898", "#29ADB2", "#0766AD"]
                solid_squares(turtle=square, colors=colors, number=squ_number)
            elif choice == "circle":
                circle = Turtle()
                cir_number = int(input("enter number of circles: ").strip())
                
                if not isinstance(cir_number, int) and cir_number > 0:
                    raise ValueError("must be positive number")
                
                colors = ["#0F0F0F", "#232D3F", "#005B41", "#008170","#04364A",
                    "#176B87", "#64CCC5", "#DAFFFB", "#C5E898", "#29ADB2", "#0766AD"]
                
                circle_canvas(turtle=circle, colors=colors, number=cir_number)
            elif choice == "triangle":
                triangle = Turtle()
                tri_number = int(input("enter number of triangles: ").strip())
                
                if not isinstance(tri_number, int) and tri_number > 0:
                    raise ValueError("must be positive number")
                
                colors = ["#0F0F0F", "#232D3F", "#005B41", "#008170","#04364A",
                    "#176B87", "#64CCC5", "#DAFFFB", "#C5E898", "#29ADB2", "#0766AD"]
                triangle_canvas(turtle=triangle, colors=colors, number=tri_number)
                
        except ValueError as e:
            print(f"\nERROR {e}\n")
            print("*" * 30)
        
        
# draw pentagon each side with a different color 
def hollow_pentagon(turtle: Turtle, colors: List[str]) -> None: 
    title("Draw of pentagon")
    turtle.speed(1)
    turtle.width(width=3)

    for color in colors:
        turtle.color(color)  # Set the color using positional argument
        turtle.forward(100)
        turtle.right(72)
    exitonclick()



# draw solid squares in different color and different locations
def solid_squares(turtle: Turtle, colors: List[str], number: int) -> None: 
    title(titlestring="draw a random numbers of solid squares")
    for _ in range(number):
        color = random.choice(colors)
        size = random.randint(50, 150)
        x_coordinate = random.randint(-300, 300)
        y_coordinate = random.randint(-390, 390)
        draw_square(turtle=turtle, color=color,size=size, x=x_coordinate, y=y_coordinate)
    exitonclick()


def draw_square(turtle: Turtle, color: str, size: int, x: int, y:int) -> None:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def circle_canvas(turtle: Turtle, colors: str, number: int) -> None:
    title(titlestring=f"draw {number} of circles")
    turtle.speed(3)
    for _ in range(number):
        color = random.choice(colors)
        radius = random.randint(50, 100)
        x_coordinate = random.randint(-250, 250)
        y_coordinate = random.randint(-350, 350)
        draw_circle(turtle=turtle, color=color,radius=radius, x=x_coordinate, y=y_coordinate)
    exitonclick()


def draw_circle(turtle: Turtle, color:str, radius: int, x:int, y:int) -> None:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius=radius)
    turtle.end_fill()


def triangle_canvas(turtle: Turtle, colors: str, number: int) -> None:
    title(titlestring=f"draw {number} of triangles")
    turtle.speed(3)
    y_coordinate = random.randint(-320, 320)
    for _ in range(number):
        color = random.choice(colors)
        size = random.randint(50, 100)
        x_coordinate = random.randint(-200, 200)
        draw_triangle(turtle=turtle, color=color,size=size, x=x_coordinate, y=y_coordinate)
    exitonclick()


def draw_triangle(turtle: Turtle, color: str, size: int, x: int, y:int) -> None:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

if __name__ == "__main__":
    main()