from random import randint
from turtle import Screen, Turtle

# Funcion 1
def raciones_venta(estacion, temp, probabilidad_de_lluvia):
    raciones = int(0)
    if (probabilidad_de_lluvia < 0.5) and (estacion == "verano"):
        raciones = 3*temp + 20*(1-probabilidad_de_lluvia)
    elif probabilidad_de_lluvia < 0.5 and estacion == "otoño":
        raciones = 2*temp + 15*(1-probabilidad_de_lluvia)
    elif probabilidad_de_lluvia < 0.5 and estacion == "invierno":
        raciones = 0.5*temp + 5*(1-probabilidad_de_lluvia)
    elif probabilidad_de_lluvia < 0.5 and estacion == "primavera":
        raciones = temp + 15*(1-probabilidad_de_lluvia)
    elif probabilidad_de_lluvia >= 0.5 and estacion == "verano":
        raciones = 2*temp + 20*(1-probabilidad_de_lluvia)
    elif probabilidad_de_lluvia >= 0.5 and estacion == "otoño":
        raciones = 2*temp + 20*(1-probabilidad_de_lluvia)
    elif probabilidad_de_lluvia >= 0.5 and estacion == "invierno":
        raciones = 0.5*temp
    elif probabilidad_de_lluvia >= 0.5 and estacion == "primavera":
        raciones = temp + 10*(1-probabilidad_de_lluvia)
    return raciones

# Segunda Funcion
def raciones_regalo(estacion, raciones_venta):
    raciones_a_regalar = 0
    if estacion == "verano":
        raciones_a_regalar = randint(1, raciones_venta//10)
    elif estacion == "otoño":
        raciones_a_regalar = randint(1, raciones_venta//8)
    elif estacion == "invierno":
        raciones_a_regalar = randint(1, raciones_venta//5)
    elif estacion == "primavera":
        raciones_a_regalar = randint(1, raciones_venta//7)
    return raciones_a_regalar

# Tercera Funcion
def dias(num):
    dia = 0
    if num == 1:
        dia = "Lunes"
    elif num == 2:
        dia = "Martes"
    elif num == 3:
        dia = "Miercoles"
    elif num == 4:
        dia = "Jueves"
    elif num == 5:
        dia = "Viernes"
    elif num == 6:
        dia = "Sabado"
    elif num == 7:
        dia = "Domingo"
    return dia

pantalla = Screen()
tortuga = Turtle()
tortuga.screen.title("Titulo")
tortuga.speed(8000000)

# Cuarta funcion
def barritas(x, y, alto, tortuga):
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
    tortuga.left(90)
    i = 0
    while i <= 1:
        tortuga.forward(alto)
        tortuga.right(90)
        tortuga.forward(80)
        tortuga.right(90)
        i += 1
    tortuga.penup()
    tortuga.forward(alto+10)
    tortuga.right(90)
    tortuga.forward(30)
    tortuga.write(int(alto/3))
    area = alto * 80
    return area

# Quinta Funcion
def texto(x, y, text, tortuga):
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.forward(25)
    tortuga.right(90)
    tortuga.forward(20)
    tortuga.write(text)
    tortuga.left(90)
    return text

# Programa Principal
print("*** El Kiwi del Mote con Huesillos ***")
i = 1
estacion = input("Estación:")
x = -350
y = -250
while i <= 7:
    print("Dia", i)
    temp = int(input("Pronóstico de temperatura: "))
    probabilidad_de_lluvia = float(input("Probabilidad de lluvia:"))
    raciones = raciones_venta(estacion, temp, probabilidad_de_lluvia)
    regalos = raciones_regalo(estacion, raciones_venta(estacion,temp, probabilidad_de_lluvia))
    print("Se producirá", int(raciones), "raciones; se regalará", regalos, "para promoción")
    alto1 = raciones * 3
    alto2 = regalos * 3
    text = dias(i)
    barritas(x, y, alto1, tortuga)
    barritas(x, y, alto2, tortuga)
    z = texto(x, y, text, tortuga)
    x += 100
    i += 1
tortuga.penup()
tortuga.goto(80000, 90000)
pantalla.exitonclick()