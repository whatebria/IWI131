def leer_perros(na):
    a = open(na)
    pe = {}
    for l in a:
        _,n,r,p,s = l.strip().split(';')
        if n not in pe:
            pe[n] = []
        pe[n].append(s)
    a.close()
    return pe
# La funcion entrega un diccionario con los nombres de los perros y el trabajo que fue realizado con ellos

def leer_razas(nombre_archivo):
    a = open(nombre_archivo)
    pe = {}
    for l in a:
        _,n,r,p,s = l.strip().split(';')
        if r not in pe:
            pe[r] = []
        pe[r].append(n)
    a.close()
    return pe

def mestizos(raza1, raza2, nombre_archivo):
    razas = leer_razas(nombre_archivo)
    mestizo = []
    for nombre1 in razas[raza1]:
        for nombre2 in razas[raza2]:
            if nombre1 == nombre2:
                mestizo.append(nombre1)
    return mestizo
print(mestizos('pequines','pastor aleman','perros.txt'))
