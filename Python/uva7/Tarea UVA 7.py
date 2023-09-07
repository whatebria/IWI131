def clasificar(tiempos, n):
    cero = 0
    listanueva = []
    for datos in tiempos:
        for i in range(len(datos)):
            if i == 1:
                dato = datos[i]
                if dato > cero:
                    listanueva.append([dato, datos[i == 0]])
                    listanueva.sort()
    l1 = []
    l2 = []
    for elemento in listanueva:
        l3 = []
        if elemento[1] not in l1:
            l1.append(elemento[1])
            l3.append(elemento[1])
            l3.append(elemento[0])
            l2.append(l3)
    clasificados = l2[:n]
    noclasificados = l2[n:]
    return [clasificados, noclasificados]

print("Bienvenidos al Gran Premio de Pythonia (Pythonia Moto Grand Prix 2022)")

# sesion de practica
tiempos = eval(input("Ingrese tiempos de la sesión de práctica: "))
print("Clasifican directamente a Q2: ",)
clasificados = clasificar(tiempos, 10)
for datos in clasificados[0]:
        print(datos[0], "con tiempo:", datos[1])

sesionq1 = eval(input("Ingrese tiempos de la sesión Q1: "))
print("Clasifican a Q2")
clasificadosq2 = clasificar(sesionq1, 2)
print(clasificadosq2[0])
print("Orden de partida del puesto 13 en adelante: ")
puesto13 = clasificar(sesionq1, 13)
puesto13 = puesto13[0]
puesto13 = puesto13[2:]
print(puesto13)

i = 0
c = 1
sesionq2 = eval(input("Ingrese tiempos de la sesión Q2: "))
calificadosq2 = clasificar(sesionq2, 20)
while i < 12:
    print(str(c) + ".", calificadosq2[0][i][0])
    i += 1
    c += 1
i2 = 0
c2 = 13
while i2 < 8:
    print(str(c2) + ".", puesto13[i2][0])
    i2+= 1
    c2+=1