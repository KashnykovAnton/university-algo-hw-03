import turtle

def draw_koch_snowflake(t, order, size):

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def setup_and_draw_snowflake(level, size = 400, color = "blue"):

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Koch Snowflake Fractal")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    t.color(color)

    for _ in range(3):
        draw_koch_snowflake(t, level, size)
        t.right(120)

    screen.exitonclick()

def main():
    while True:
        try:
            level = int(input("Enter recursion level (non-negative integer): "))
            if level >= 0:
                break
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Please enter a valid integer.")

    setup_and_draw_snowflake(level)

if __name__ == "__main__":
    main()
