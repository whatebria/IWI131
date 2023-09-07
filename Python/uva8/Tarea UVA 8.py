def comunas_con_mas_oferta(lista, operacion):
    lista2 = []
    dic = {}
    for id, tipo, op, comuna, dorm, banos, es, m2, pis, gym, precio in lista:
        if operacion == op:
            lista2.append(comuna)
    for datos in lista2:
        if datos not in dic:
            dic[datos] = 0
        dic[datos] += 1
    lista3 = []
    lista4 = []
    for datos in dic:
        if datos not in lista3:
            lista3.append([dic[datos], datos])
            lista3.sort()
            lista3.reverse()
    for dato in lista3:
        lista4.append(dato[1])
    return lista4[:3]

def filtrar(lista, tipo, op, min_dorm, min_m2):
    r = {}
    for datos in lista:
        if datos[3] not in r and datos[1] == tipo and op == datos[2] and datos[4] >= min_dorm and datos[7] >= min_m2:
            r[datos[3]] = []
        if datos[1] == tipo and op == datos[2] and datos[4] >= min_dorm and datos[7] >= min_m2:
            r[datos[3]] += [[datos[10], datos[0], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9]]]
    for dato in r:
        if r[dato] == []:
            del r[dato]
    return r

def buscar(oferta,solicitudes):
    dic = {}
    lista = []
    for datos in solicitudes:
        filtro = filtrar(oferta, datos[1][0], datos[1][1], datos[1][2], datos[1][3])
        for keys in filtro:
            lista.append(keys)
            lista.append(filtro[keys])
            dic[datos[0]] = lista
    lista1 = []
    for butt in dic:
        lista1.append(butt)
        lista1.append(lista)
    return lista1