def filtrar(na, consola, minima):
    archivo = open(na, 'r')
    archivoconsola = open(f"{consola}.txt", "w")
    juegos = 0
    for datos in archivo:
        t, j, g, d, ca, p, co, e, a = datos.strip().split(";")
        if co == consola and int(ca) >= minima:
            archivoconsola.write(t + '(' + g + '), de ' + d + '(' + a + '), con nota: ' + ca + '\n')
            juegos += 1
    archivo.close()
    return juegos

def rankear(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    juegos = []
    generos = []
    for datos in archivo:
        t, j, g, d, ca, p, co, e, a = datos.strip().split(";")
        if t not in juegos:
            juegos.append([ca, g, t, co])
        if g not in generos:
            generos.append(g)
    for datos in juegos:
        gen = datos[1]
    i = 0
    while i < len(generos)-1:
        archivo = open("{}.txt".format(generos[i]), "w")
        i+=1
        i = 0
        for datos in generos:
            if datos == gen:
                archivo.write("hola|")
        i += 1
print(rankear('juegos.txt'))
