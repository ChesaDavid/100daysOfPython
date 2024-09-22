import time
import turtle

def slow_turtle_print(text, delay=0.1):
    """Draw text slowly on Turtle screen."""
    screen = turtle.Screen()
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-200, 0)  
    pen.pendown()

    for char in text:
        pen.write(char, move=False, align="left", font=("Arial", 24, "normal"))
        time.sleep(delay)
        pen.setx(pen.xcor() + 15)  

    screen.mainloop()

def read_file_content(filename):
    """Read the content from a file."""
    with open(filename, 'r') as file:
        content = file.read()
    return content

file_content = read_file_content('input.txt')

slow_turtle_print(file_content, delay=0.15)
