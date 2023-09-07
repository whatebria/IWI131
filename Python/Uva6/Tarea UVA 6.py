from random import randint

# Función 1
def generar_universo(size):
    consonantes = "bcdfghjklmnpqrstvwxyz"  # 21
    vocales = "aeiou"  # 4
    texto = ""
    c = 0
    while c < round(size * 0.4):
        n = randint(0, 4)
        letra = vocales[n]
        texto += letra
        c += 1
    c = 0
    while c < round(size * 0.6):
        n = randint(0, 20)
        letra = consonantes[n]
        texto += letra
        c += 1
    if size < 10 or size > 35:
        texto = ""
    return texto

# Funcion contador vocales
def cant_vocales(palabra):
    vocales = "aeiou"
    i = 0
    for letras in palabra:
        if letras in vocales:
            i += 1
    return i

# Funcion contador consonantes
def can_consonantes(palabra):
    consonantes = "bcdfghjklmnpqrstvwxyz"  # 21
    c = 0
    for letras in palabra:
        if letras in consonantes:
            c += 1
    return c

# Funcion contar letras
def c_letras (letras, palabra):
    c = 0
    for caract in palabra:
        if caract == letras:
            c += 1
    return c

# Programa
print("Bienvenido al PysCrable")

tamano_universo = int(input("Ingrese el tamaño del universo de letras: "))

# Printeo Universo
while tamano_universo < 10:
    tamano_universo = int(input("Ingrese el tamaño del universo de letras: "))
if tamano_universo >= 10:
    #universo = generar_universo(tamano_universo)
    universo = "qlhswdmwbvtsuaoeeaoi"
    print("Universo:", universo)

palabras = input("Ingrese sus 3 palabras separadas por un guión: ")

# Posicion del guion
c = 0
for letra in palabras:
    if letra == "-":
        pg2 = c
    c += 1
c = -1
for letra in palabras:
    if letra == "-":
        pg1 = c
    c -= 1

# Palabras
palabra1 = palabras[:pg1]
palabra2 = palabras[pg1+1:pg2]
palabra3 = palabras[pg2+1:]
puntaje1 = 0
puntaje2 = 0
puntaje3 = 0
total = 0

invalido = False
# # Palabra 1
if len(palabra1) >= 3 and invalido == False:
    puede = True
    for letra in palabra1:
        if not c_letras(letra, universo) >= c_letras(letra, palabra1):
            puede = False
    print(palabra1, "se puede generar con", universo)
    puntaje1 = (len(palabra1) * 10) + (5 * cant_vocales(palabra1)) + (3 * can_consonantes(palabra1))
    print("Obtienes", puntaje1, "puntos")
    total += puntaje1
if len(palabra1) < 3:
    print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
    total = 0
    invalido = True

#Palabra 2
if len(palabra2) >= 3 and invalido == False:
    puede = True
    for letra in palabra2:
        if not c_letras(letra, universo) >= c_letras(letra, palabra2):
            puede = False
    print(palabra2, "se puede generar con", universo)
    puntaje2 = (len(palabra2) * 10) + (5 * cant_vocales(palabra2)) + (3 * can_consonantes(palabra2))
    print("Obtienes", puntaje2, "puntos")
    total += puntaje2
elif len(palabra2) < 3:
    print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
    total = 0
    invalido = True

# Palabra 3
if len(palabra3) >= 3 and invalido == False:
    puede = True
    for letra in palabra3:
        if not c_letras(letra, universo) >= c_letras(letra, palabra3):
            puede = False
    print(palabra3, "se puede generar con", universo)
    puntaje3 = (len(palabra3) * 10) + (5 * cant_vocales(palabra3)) + (3 * can_consonantes(palabra3))
    print("Obtienes", puntaje3, "puntos")
    total += puntaje3
elif len(palabra3) < 3:
    print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
    total = 0
    invalido = True
print("Fin del intento, obtuviste un total de", total, "puntos")
