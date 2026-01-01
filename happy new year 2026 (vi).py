#happy new year 2026!!!
import turtle
import random
import time
window = turtle.Screen()
window.bgcolor("black")
window.title("Chúc Mừng Năm Mới 2026!")
window.setup(width=800, height=600)
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.speed(0)
text_turtle.penup()
fireworks = []
def create_firework(x, y, color):
    firework = turtle.Turtle()
    firework.hideturtle()
    firework.speed(0)
    firework.penup()
    firework.goto(x, y)
    firework.color(color)
    firework.pendown()
    for _ in range(36):
        firework.forward(50)
        firework.backward(50)
        firework.left(10)
    fireworks.append(firework)
def display_new_year_message():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]
    text_turtle.goto(0, 200)
    text_turtle.color("gold")
    text_turtle.write("CHÚC MỪNG NĂM MỚI", align="center", font=("Arial", 36, "bold"))
    text_turtle.goto(0, 140)
    text_turtle.color("red")
    text_turtle.write("2026", align="center", font=("Arial", 48, "bold"))  # ĐÃ ĐỔI
    text_turtle.goto(0, 50)
    text_turtle.color("cyan")
    text_turtle.write("AN KHANG THỊNH VƯỢNG", align="center", font=("Arial", 24, "normal"))
    text_turtle.goto(0, 10)
    text_turtle.color("lightgreen")
    text_turtle.write("VẠN SỰ NHƯ Ý", align="center", font=("Arial", 24, "normal"))
    text_turtle.goto(0, -30)
    text_turtle.color("pink")
    text_turtle.write("TẤN TÀI TẤN LỘC", align="center", font=("Arial", 24, "normal"))
    text_turtle.goto(0, -100)
    text_turtle.color("yellow")
    text_turtle.write("HAPPY NEW YEAR!", align="center", font=("Arial", 28, "bold"))
def draw_peach_flower(x, y, size):
    flower = turtle.Turtle()
    flower.hideturtle()
    flower.speed(0)
    flower.penup()
    flower.goto(x, y)
    flower.pendown()
    flower.color("pink")
    flower.fillcolor("pink")
    flower.begin_fill()
    for _ in range(5):
        flower.forward(size)
        flower.right(144)
    flower.end_fill()
    flower.penup()
    flower.goto(x + size/2, y - size/3)
    flower.pendown()
    flower.color("yellow")
    flower.dot(size/2)
    return flower
def draw_lucky_money(x, y, width, height):
    envelope = turtle.Turtle()
    envelope.hideturtle()
    envelope.speed(0)
    envelope.penup()
    envelope.goto(x, y)
    envelope.pendown()
    envelope.color("red")
    envelope.fillcolor("red")
    envelope.begin_fill()
    for _ in range(2):
        envelope.forward(width)
        envelope.left(90)
        envelope.forward(height)
        envelope.left(90)
    envelope.end_fill()
    envelope.penup()
    envelope.goto(x, y + height)
    envelope.pendown()
    envelope.begin_fill()
    envelope.goto(x + width/2, y + height + width/3)
    envelope.goto(x + width, y + height)
    envelope.goto(x, y + height)
    envelope.end_fill()
    envelope.penup()
    envelope.goto(x + width/2, y + height/2)
    envelope.pendown()
    envelope.color("gold")
    envelope.write("LỘC", align="center", font=("Arial", 14, "bold"))
    return envelope
def draw_kumquat(x, y, size):
    kumquat = turtle.Turtle()
    kumquat.hideturtle()
    kumquat.speed(0)
    kumquat.penup()
    kumquat.goto(x, y)
    kumquat.pendown()
    kumquat.color("orange")
    kumquat.fillcolor("orange")
    kumquat.begin_fill()
    kumquat.circle(size)
    kumquat.end_fill()
    return kumquat
def draw_new_year_scene():
    display_new_year_message()
    flowers = []
    flower_positions = [(-300, -150), (-200, -100), (200, -150), (300, -100)]
    for pos in flower_positions:
        flowers.append(draw_peach_flower(pos[0], pos[1], 30))
    envelopes = []
    envelope_positions = [(-350, 100), (-100, -200), (150, -200)]
    for pos in envelope_positions:
        envelopes.append(draw_lucky_money(pos[0], pos[1], 60, 90))
    kumquats = []
    kumquat_positions = [(-150, 150), (0, 180), (100, 150)]
    for pos in kumquat_positions:
        kumquats.append(draw_kumquat(pos[0], pos[1], 15))
    return flowers, envelopes, kumquats
def create_random_fireworks(count):
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "cyan", "magenta"]
    for _ in range(count):
        x = random.randint(-350, 350)
        y = random.randint(-200, 200)
        color = random.choice(colors)
        create_firework(x, y, color)
def clear_fireworks():
    for firework in fireworks:
        firework.clear()
        firework.hideturtle()
    fireworks.clear()
def main():
    flowers, envelopes, kumquats = draw_new_year_scene()
    create_random_fireworks(5)
    counter = 0
    try:
        while True:
            if counter % 50 == 0:
                create_random_fireworks(2)
            if counter % 100 == 0 and len(fireworks) > 10:
                clear_fireworks()
                create_random_fireworks(3)
            if counter % 30 == 0:
                text_turtle.clear()
                display_new_year_message()
            counter += 1
            window.update()
            time.sleep(0.05)
    except:
        print("Một chút nuối tiếc còn lại, hãy để lại ở năm 2025. Cùng đến với năm 2026-một năm tràn đầy hạnh phúc, vui vẻ, thành công ở bên cả gia đình và người thân. Happy new year 2026!")
if __name__ == "__main__":
    main()
    turtle.done()