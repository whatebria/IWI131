doc = open('postulantes.txt')
ife = 0
ifetotal = 0
listapostulantes = []
for n in doc:
    n = n.strip().split(';')
    fechatrabajo = n[4].split('-')
    if int(n[1]) >= 18 and int(n[-1]) <= 1140000 and ((int(fechatrabajo[0]) == 2021 and int(fechatrabajo[1]) >= 7) or
                                                      (int(fechatrabajo[0]) == 2022 and int(fechatrabajo[1]) <= 3)):
        if (n[2] == 'M' and int(n[1]) <= 23 or int(n[1]) >=55) or (n[2] == 'F'):
            ife = round(0.45 * int(n[-1]) * 3)
            if ife > 1000000:
                ife = 1000000
            ifetotal += ife
            listapostulantes.append([ife, n[-1], n[-3], n[1]])
        elif n[2] == 'M' and 24 <= int(n[1]) <= 55:
            ife = round(0.35 * int(n[-1]) * 3)
            if ife > 750000:
                ife = 750000
            ifetotal += ife
            listapostulantes.append([ife, n[-1], n[-3], n[1]])
listapostulantes.sort()
listapostulantes.reverse()
parametros = open('rangos.txt')
edadmayor = 0
listaderangos = []
personas = 0
for datos in listapostulantes:
    if int(datos[-1]) >= edadmayor:
        edadmayor = int(datos[-1])
for lentejas in parametros:
    listaderangos.append(lentejas.strip())
listaderangos.append(str(edadmayor))
listaderangos.insert(0, '17')
contador = 0
while contador < len(listaderangos)-1:
    resumenes = open(f'resumen_{int(listaderangos[contador]) + 1}_{listaderangos[contador + 1]}.txt', 'w')
    for queso in listapostulantes:
        if int(listaderangos[contador]) + 1 <= int(queso[-1]) <= int(listaderangos[contador + 1]):
            resumenes.write(str(queso[2]) + ' ' + str(queso[1]) + ' ' + str(queso[0]) + '\n')
    contador += 1
resumenes.close()
archivoestadisticas = open('estadisticas.txt', 'w')
archivoestadisticas.write('Resultado de la asignación del IFE \n')
archivoestadisticas.write('Monto total asignado: ' + str(ifetotal) + '\n')
archivoestadisticas.write('Beneficiarios: ' + str(len(listapostulantes)) + '\n')
archivoestadisticas.write('Distribución por rangos de edad:  \n')
contador = 0
while contador < len(listaderangos)-1:
    personas = 0
    iferangos = 0
    for queso in listapostulantes:
        if int(listaderangos[contador]) + 1 <= int(queso[-1]) <= int(listaderangos[contador + 1]):
            personas += 1
            iferangos += int(queso[0])
    archivoestadisticas.write(f'Las personas entre' + str(int(listaderangos[contador])+1) + 'y' +
                              str(listaderangos[contador + 1]) + ' años representan un ' + str(personas*100/len(listapostulantes)) + '% del total de personas. \n')
    archivoestadisticas.write('La asignación para este rango corresponde a un ' + str(round((iferangos*100)/ifetotal, 2)) + ' del monto total asignado. \n \n')
    contador += 1
archivoestadisticas.close()