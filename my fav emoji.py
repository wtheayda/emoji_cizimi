import turtle

# Ekran
ekran = turtle.Screen()
ekran.setup(width=800, height=600)
ekran.bgcolor("#cceeff")
ekran.title("⛅🌈 ")

# Kalem
kalem = turtle.Turtle()
kalem.speed(0)
kalem.pensize(3)

# Güneş
def gunes_ciz(x, y, yaricap):
    kalem.penup()
    kalem.goto(x, y - yaricap)
    kalem.pendown()
    kalem.color("yellow")
    kalem.circle(yaricap)

    kalem.color("orange")
    for i in range(12):
        kalem.penup()
        kalem.goto(x, y)
        kalem.setheading(i * 30)
        kalem.forward(yaricap)
        kalem.pendown()
        kalem.forward(20)

# Bulut
def bulut_ciz(x, y):
    kalem.color("deepskyblue")
    offsets = [-30, 0, 30, 60]
    yaricaplar = [20, 25, 20, 15]

    for i in range(len(offsets)):
        kalem.penup()
        kalem.goto(x + offsets[i], y)
        kalem.pendown()
        kalem.circle(yaricaplar[i])

    for i in range(len(offsets)):
        kalem.penup()
        kalem.goto(x + offsets[i] + 10, y - 20)
        kalem.pendown()
        kalem.circle(15)

# Gökkuşağı (yatay parabolik)
def gokkusagi_yatay_yay(x, y, buyukluk):
    renkler = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    kalem.width(8)

    for i, renk in enumerate(renkler):
        kalem.penup()
        kalem.goto(x, y - i * 10)
        kalem.setheading(90)  # yukarı yönlü yay
        kalem.pendown()
        kalem.color(renk)
        kalem.circle(buyukluk - i * 10, 180)

    kalem.width(1)

# Konumlar
gunes_ciz(-120, 80, 40)            # solda güneş
bulut_ciz(-40, 100)                # ekranın ortasında bulut
gokkusagi_yatay_yay(-200, -120, 250)  # ekranın alt kısmında gökkuşağı

kalem.hideturtle()
turtle.done()
