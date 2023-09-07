print("*** Kiwi ayuda al Coyote ***")
print("Ingrese los siguientes datos:")

# con minusculas son los iniciales
xc = float(input("Cordenada del correcaminos:"))
vi = float(input("Velocidad inicial de lanzamiento (kms/h):"))
al = float(input("Ángulo de lanzamiento, expresado (grados):"))
xi = float(input("Coordenada x del lanzamiento (Coyote):"))
yi = float(input("Coordenada y del lanzamiento (Coyote):"))

print("Valores ajustados:")

# con mayusculas ajustados
V = float(vi*10/36)
print("Velocidad =", V, "m/s")

from math import pi, cos, sin, sqrt
Al = float(al*pi/180)
print("Ángulo de lanzamiento =", round(Al, 5), "radianes")

Vx = float(V*cos(Al))
print("vx =", round(Vx, 5), "m/s")

Vy = float(V*sin(Al))
print("vy =", round(Vy, 5), "m/s")

print("Evaluación del lanzamiento:")

# yi + vyt – 4.9t**2 = 0

a = float(-4.9)
b = float(Vy)
c = float(yi)
d = float((b**2)-(4*a*c))
x1 = (-b-(d**(1/2)))/(2*a)

print("Tiempo de impacto estimado:", round(x1, 5), "s")

# tiempo 0
y0 = ((a*(0**2)) + (b*0) + c)
x0 = xi + Vx * 0
print("En tiempo 0 el proyectil se encuentra en:", round(x0, 5), round(y0, 5))

# tiempo 0.1
y01 = ((a*0.1**2) + (b*0.1) + c)
x01 = xi + Vx * 0.1
print("En tiempo 0.1 el proyectil se encuentra en: ", round(x01, 5), round(y01, 5))

# tiempo 0.2
y02 = ((a*0.2**2) + (b*0.2) + c)
x02 = xi + Vx * 0.2
print("En tiempo 0.2 el proyectil se encuentra en: ", round(x02, 5), round(y02, 5))

# tiempo 0.3
# x(t) = xi + vxt
y03 = ((a*0.3**2) + (b*0.3) + c)
x03 = xi + Vx * 0.3
print("En tiempo 0.3 el proyectil se encuentra en: ", round(x03, 5), round(y03, 5))

t1 = float(x1 - 0.1)
t2 = float(x1 - 0.2)
t3 = float(x1 - 0.3)

y11 = ((a*t1**2) + (b*t1) + c)
x11 = xi + Vx * t1

y2 = ((a*t2**2) + (b*t2) + c)
x2 = xi + Vx * t2

y3 = ((a*t3**2) + (b*t3) + c)
x3 = xi + Vx * t3

print("En tiempo", round(t1, 5), "el proyectil se encuentra en:", round(x3, 5), round(y3, 5))
print("En tiempo", round(t2, 5), "el proyectil se encuentra en:", round(x2, 5), round(y2, 5))
print("En tiempo", round(t3, 5), "el proyectil se encuentra en:", round(x11, 5), round(y11, 5))


impactox = xi + Vx * x1
print("Proyectil impacta en coordenada x:", round(impactox, 5))

f = float(impactox - xc)
print("Se falló al Correcaminos por:", round(f, 5), "m")