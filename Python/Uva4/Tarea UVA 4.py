from random import randint
from math import sqrt

print("Bienvenid@s a GimnasIWI!")
m = int(input("Ingrese meta en calorias:"))
c = 0
total = 0
flag = True

while (m > total) and (flag == True):
    print("Ingrese ejercicio")
    print("(1) Sentadillas sumo")
    print("(2) Plancha abdominal")
    print("(3) Press frances")
    print("(4) Me canse")
    e = int(input(""))
    if e == 1:
        r = int(input("¿Cuantas repeticiones?: "))
        numero_random = 3 #randint(3,7)
        cq = int(r * numero_random)
        print("Calorias quemadas con sentadillas: ", cq)
        total += cq
        total = round(total)
        print("Calorias hasta el momento: ", total)
    elif e == 2:
        s = int(input("Cuantos segundos?: "))
        n = 1
        suma = 0
        while s >= n:
            factorial = 1
            c = 1
            while c <= n:
                factorial *= c
                c += 1
            suma += (4 ** n) / factorial
            n += 1
        total += suma
        total = round(total)
        print("Calorias quemadas con plancha: ", round(suma))
        print("Calorias hasta el momento: ", round(total))
    elif e == 3:
        reps = int(input("¿Cuantas repeticiones?: "))
        kilos = int(input("¿Cuantos kilos?: "))
        i = 1
        if reps < kilos:
            resultado = kilos
            primer_termino = kilos
            while i < reps:
                calculo = 1 + sqrt(primer_termino)
                resultado += calculo
                primer_termino = calculo
                i += 1
            print("Calorias quemadas con press frances:", (round(resultado)))
            total += resultado
            total = round(total)
            print("Calorias hasta el momento:", total)
        if kilos < reps:
            resultado = reps
            primer_termino = reps
            while i < kilos:
                calculo = 1 + sqrt(primer_termino)
                resultado += calculo
                primer_termino = calculo
                i += 1
            print("Calorias quemadas con press frances:", (round(resultado)))
            total += resultado
            total = round(total)
            print("Calorias hasta el momento:", total)
    elif e == 4:
        print("************")
        print("A descansar! Quemaste ", round(total), "calorias")
        flag = False
    else:
        print("Ingrese una opcion valida")
if flag == True:
    print("************")
    print("Meta cumplida! Quemaste", total, "de un total de", m, "calorias")