import turtle

def draw_certificate(name, gpa):
    screen = turtle.Screen()
    screen.title("Certificate")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(3)
    pen.pensize(2)
    pen.hideturtle()

    # Draw certificate border
    pen.penup()
    pen.goto(-150, 100)  # top-left corner of 300x200 box
    pen.pendown()
    pen.pensize(5)
    for _ in range(2):
        pen.forward(300)  # width
        pen.right(90)
        pen.forward(200)  # height
        pen.right(90)

    # Write certificate title
    pen.penup()
    pen.goto(0, 70)
    pen.color("blue")
    pen.write("Certificate of Achievement", align="center", font=("Arial", 18, "bold"))

    # Write student's name
    pen.goto(0, 40)
    pen.color("black")
    pen.write(f"Awarded to: {name}", align="center", font=("Arial", 14, "normal"))

    # Write GPA
    pen.goto(0, 15)
    pen.write(f"GPA: {gpa:.2f}", align="center", font=("Arial", 14, "normal"))

    # Draw a star decoration
    pen.goto(0, -40)
    pen.color("gold")
    pen.setheading(0)
    pen.begin_fill()
    for _ in range(5):
        pen.forward(40)
        pen.right(144)
    pen.end_fill()

    # Write footer
    pen.goto(0, -80)
    pen.color("black")
    pen.write("Top Student", align="center", font=("Arial", 12, "bold"))

    screen.mainloop()
