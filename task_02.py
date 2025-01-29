import turtle

def draw_koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Запит у користувача на рівень рекурсії
    while True:
        try:
            level = int(input("Введіть рівень рекурсії (ціле число більше або рівне 0): "))
            if level >= 0:
                break
            else:
                print("Будь ласка, введіть ціле число більше або рівне 0.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    # Ініціалізація вікна та черепахи
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.color("blue")

    # Виклик функції для малювання сніжинки Коха
    for _ in range(3):
        draw_koch_snowflake(t, level, 400)
        t.right(120)

    # Закриваємо вікно при кліку
    screen.exitonclick()

if __name__ == "__main__":
    main()
