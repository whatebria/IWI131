from random import randint
vs = 25000
ds = 27000
vd = 22000
viernes = 50000
sabado = 75000
domingo = 60000
dia = 0
dia1 = 0
dia2 = 0
estacionamiento = 0

print("Bienvenido a LolaPYlooza")
print("------- Sistema de cotización de entradas -------------")
print()
total = 0
cd = int(input("Cantidad de días:"))

# 1 dia

if cd == 1:
    dia = input("Día que desea asistir:")

# 2 dias

elif cd == 2:
    dia1 = input("Día 1 que desea asistir:")
    dia2 = input("Día 2 que desea asistir: ")

# 3 dias

if cd == 3:
    print("Total a pagar por todos los días $ 150000")
    total = total + 150000


# valores 1 dia

if cd == 1 and dia == "Viernes":
    print("Día 1: Viernes Valor $ 50000")
    total = total+viernes
elif cd == 1 and dia == "Sábado":
    print("Día 1: Sabado Valor $ 75000")
    total = total + sabado
elif cd == 1 and dia == "Domingo":
    print("Día 1: Domingo Valor $ 60000")
    total = total + domingo

# valores dos dias

if cd == 2 and dia1 == "Viernes" and dia2 == "Sábado":
    print("Día 1: Viernes Valor $ ", viernes)
    print("Día 2: Sábado Valor $ ", sabado)
    total = total + viernes + sabado
elif cd == 2 and dia1 == "Sábado" and dia2 == "Viernes":
    print("Día 1: Sábado Valor $ ", sabado)
    print("Día 2: Viernes Valor $ ", viernes)
    total = total + viernes + sabado

elif cd == 2 and dia1 == "Sábado" and dia2 == "Domingo":
    print("Día 1: Sábado Valor $ ", sabado)
    print("Día 2: Domingo Valor $ ", domingo)
    total = total + domingo + sabado
elif cd == 2 and dia1 == "Domingo" and dia2 == "Sábado":
    print("Día 1: Domingo Valor $ ", domingo)
    print("Día 2: Sábado Valor $ ", sabado)
    total = total + domingo + sabado

elif cd == 2 and dia1 == "Domingo" and dia2 == "Viernes":
    print("Día 1: Domingo Valor $ ", domingo)
    print("Día 2: Viernes Valor $ ", viernes)
    total = total + domingo + viernes
elif cd == 2 and dia1 == "Viernes" and dia2 == "Domingo":
    print("Día 1: Viernes Valor $ ", viernes)
    print("Día 2: Domingo Valor $ ", domingo)
    total = total + domingo + viernes


# decuento dos dias
dcto = 0.2
if cd == 2 and dia1 == "Viernes" and dia2 == "Sábado":
    print("Descuento por días:", int((viernes + sabado) * dcto))
    total = total - ((viernes + sabado) * dcto)
elif cd == 2 and dia1 == "Sábado" and dia2 == "Viernes":
    print("Descuento por días:", int((viernes + sabado) * dcto))
    total = total - ((viernes + sabado) * dcto)


elif cd == 2 and dia1 == "Sábado" and dia2 == "Domingo":
    print("Descuento por días:", int((domingo + sabado) * dcto))
    total = total - ((domingo + sabado) * dcto)
elif cd == 2 and dia1 == "Domingo" and dia2 == "Sábado":
    print("Descuento por días:", int((domingo + sabado) * dcto))
    total = total - ((domingo + sabado) * dcto)

elif cd == 2 and dia1 == "Domingo" and dia2 == "Viernes":
    print("Descuento por días:", int((viernes + domingo) * dcto))
    total = total - ((viernes + domingo) * dcto)
elif cd == 2 and dia1 == "Viernes" and dia2 == "Domingo":
    print("Descuento por días:", int((domingo + sabado) * dcto))
    total = total - ((domingo + viernes) * dcto)


# si elige vip 1 dia

r = 0.4

vip = int(input("Ingrese 1 si desea entrada vip:"))

if cd == 1 and vip == 1 and dia == "Viernes":
    print("Recargo por entrada VIP $", int(viernes*r))
    total = total + (viernes*r)
elif cd == 1 and vip == 1 and dia == "Sábado":
    print("Recargo por entrada VIP $", int(sabado*r))
    total = total + (sabado * r)
elif cd == 1 and vip == 1 and dia == "Domingo":
    print("Recargo por entrada .VIP $", int(domingo*r))
    total = total + (domingo * r)
# Si elige vip 2 dias

elif cd == 2 and dia1 == "Domingo" and dia2 == "Sábado" and vip == 1:
    print("Recargo por entrada VIP $", int(((domingo + sabado)-ds)*r))
    total = total + (((domingo + sabado)-ds)*r)
elif cd == 2 and dia1 == "Sábado" and dia2 == "Domingo" and vip == 1:
    print("Recargo por entrada VIP $", int(((domingo + sabado)-ds)*r))
    total = total + (((domingo + sabado) - ds)*r)

elif cd == 2 and dia1 == "Viernes" and dia2 == "Domingo" and vip == 1:
    print("Recargo por entrada VIP $", int(((domingo + viernes)-vd)*r))
    total = total + (((domingo + viernes) - vd)*r)
elif cd == 2 and dia1 == "Domingo" and dia2 == "Viernes" and vip == 1:
    print("Recargo por entrada VIP $", int(((domingo + viernes)-vd)*r))
    total = total + (((domingo + viernes) - vd)*r)

elif cd == 2 and dia1 == "Sábado" and dia2 == "Viernes" and vip == 1:
    print("Recargo por entrada VIP $", int(((viernes + sabado)-vs)*r))
    total = total + (((viernes + sabado) - vs)*r)
elif cd == 2 and dia1 == "Viernes" and dia2 == "Sábado" and vip == 1:
    print("Recargo por entrada VIP $", int(((viernes + sabado)-vs)*r))
    total = total + (((viernes + sabado) - vs)*r)

# Si quiere vip y va los 3 dias

elif cd == 3 and vip == 1:
    print("Recargo por entrada VIP $ 60000")
    total = total + 60000

# Si no quieren vip y quieren estacionamiento

if vip == 0:
    estacionamiento = int(input("Ingrese 1 se desea estacionamiento:"))

if cd == 1 and vip != 1 and estacionamiento != 0:
    print("Recargo por estacionamiento $ 10000")
    total = total + 10000
elif cd == 2 and vip != 1 and estacionamiento != 0:
    print("Recargo por estacionamiento $ 20000")
    total = total + 20000
elif cd == 3 and vip != 1 and estacionamiento != 0:
    print("Recargo por estacionamiento $ 30000")
    total = total + 30000

# Pagara con tarjeta
tarjeta = int(input("Ingrese 1 si tiene tarjeta Banco Pythonia:"))

dctorandom = randint(0, 10)
if tarjeta == 1:
    print("Descuento por cliente Bco Pythonia:", int((total * 30)/100))
    total = total - ((total * 30)/100)
    print("Total a pagar: $", int(total))
elif tarjeta != 1:
    print("Descuento por sorteo:", dctorandom, "% equivalente a", int(total * (dctorandom/100)))
    total = total - (total * (dctorandom/100))
    print("Total a pagar: $", int(total))
