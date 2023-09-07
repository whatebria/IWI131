archivo = open('postulantes.txt')
lista = []
for linea in archivo:
    a = linea.strip().replace('-', ';')
    dato = a.strip().split(';')
    if int(dato[6]) >= 7 and dato[5] == '2021' and int(dato[2]) >= 18 and int(dato[-1]) <= 1140000:
        lista.append(dato)
    if int(dato[6]) <= 3 and dato[5] == '2022' and int(dato[2]) >= 18 and int(dato[-1]) <= 1140000:
        lista.append(dato)
archivo.close()
personas = []
ife = 0
ifeacumulado = 0
for datos in lista:
    if datos[3] == 'F':
        ife = round(((45 / 100) * int(datos[-1])) * 3)
        if ife > 1000000:
            ife = 1000000
        ifeacumulado += ife
        personas.append([ife, int(datos[-1]), datos[4], int(datos[2])])
    if datos[3] == 'M' and (int(datos[2]) <= 23 or int(datos[2]) > 55):
        ife = round(((45 / 100) * int(datos[-1])) * 3)
        if ife > 1000000:
            ife = 1000000
        ifeacumulado += ife
        personas.append([ife, int(datos[-1]), datos[4], int(datos[2])])
    if datos[3] == 'M' and 23 < int(datos[2]) <= 55:
        ife = round(((35 / 100) * int(datos[-1])) * 3)
        if ife > 750000:
            ife = 750000
        ifeacumulado += ife
        personas.append([ife, int(datos[-1]), datos[4], int(datos[2])])
personas.sort()
personas.reverse()
mayor = 0
for datos in lista:
    if int(datos[2]) > mayor:
        mayor = int(datos[2])
r = open('rangos.txt')
rangos = []
for n in r:
    n = n.strip()
    if n not in rangos:
        rangos.append(int(n))
rangos.insert(0, 17)
rangos.append(mayor)
i = 0
while i < len(rangos)-1:
    archivo = open(f'resumen_{rangos[i] + 1}_{rangos[i + 1]}.txt', 'w')
    for lineas in personas:
        if rangos[i]+1 <= lineas[-1] <= rangos[i + 1]:
            archivo.write(str(lineas[2]) + ' ' + str(lineas[1]) + ' ' + str(lineas[0]) + '\n')
    i += 1
archivo.close()
estadistica = open('estadisticas.txt', 'w')
estadistica.write('Resultado de la asignación del IFE ' + '\n')
estadistica.write('Monto total asignado: ' + str(ifeacumulado) + '\n')
estadistica.write('Beneficiarios: ' + str(len(personas)) + '\n')
estadistica.write('\n' + 'Distribución por rangos de edad: ' + '\n' + '\n')
i = 0
while i < len(rangos)-1:
    cantidaddepersonas = 0
    iferangos = 0
    for queso in personas:
        if int(rangos[i]) + 1 <= int(queso[-1]) <= int(rangos[i + 1]):
            cantidaddepersonas += 1
            iferangos += int(queso[0])
    estadistica.write(f'Las personas entre' + str(int(rangos[i])+1) + 'y' + str(rangos[i + 1]) + ' años representan un ' + str((cantidaddepersonas)*100/len(personas)) + '% del total de personas. \n')
    estadistica.write('La asignación para este rango corresponde a un ' + str(round((iferangos*100)/ifeacumulado, 2)) + ' del monto total asignado. \n \n')
    i += 1
estadistica.close()