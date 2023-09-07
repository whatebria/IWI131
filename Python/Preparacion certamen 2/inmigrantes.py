def filtrar(nombre_archivo, año):
    archivo = open(nombre_archivo, "r")
    dicc = {}
    for linea in archivo:
        campos = linea.strip().split(":")
        fecha = campos[3].split("-")
        nombre = campos[1]
        pais = campos[2]
        if pais not in dicc:
            dicc[pais] = []
        if int(fecha[2]) == año:
            dicc[pais].append(nombre)
    archivo.close()
    return dicc
print(filtrar(f"inmigrantes.txt",2019))

def contar_ingresos(nombre_archivos, año):
    dic_contador = {}
    personas = filtrar(nombre_archivos, año)
    for keys in personas:
        if keys not in dic_contador:
            dic_contador[keys] = len(personas[keys])
        if dic_contador[keys] == 0:
            del dic_contador[keys]
    return dic_contador
print(contar_ingresos("inmigrantes.txt",2019))

def escribir_ingresos(nombre_archivos, año):
    archivoingresos = open("ingresos {año}.txt", "w")
    ingresos = contar_ingresos(nombre_archivos, año)
    lista = []
    cant_de_ingresos = 0
    for key in ingresos:
        lista.append([ingresos[key], key])
        lista.sort()
        lista.reverse()
    for datos in lista:
        cant_de_ingresos += datos[0]
    c = 0
    while c < len(lista):
        archivoingresos.write(str(c+1) + "-" + str(lista[c][1] + ":" + str(lista[c][0])) + "\n")
        c += 1
    return cant_de_ingresos
print(escribir_ingresos("inmigrantes.txt",2019))

