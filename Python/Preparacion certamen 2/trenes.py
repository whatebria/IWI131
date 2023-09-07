lineaP = [
'Estacion Central' ,
'Puente Sal y Santo' ,
'Pytronato' ,
'La Pysterna' ,
'Pynstein' ,
'Estadio Nacional' ,
'Pio-Pio' ,
'Plaza Python Alto']

tipos = {'Expreso': ['E07','F07','F08', ...],
         'Normal' : ['G00','H00', ...],
         'Corto' : ['B00','C01', ...]}

trenes = {'E07':['09','03'],'F07':['10','14'],
          'H00':['09','23'], 'B00':['08','00'],
          'G00':['08','46'],'C01':['13','59'],
          'F08':['11','02'] }

def tiempodellegada(tipo, linea, listadelineas):
    llegada = 0
    lin = []
    for lineas in listadelineas:
        lin.append([listadelineas.index(lineas)+1, lineas])
    for dato in lin:
        if tipo == "expreso" and linea == dato[1]:
            llegada = 2 * dato[0]
        elif tipo == "normal" and linea == dato[1]:
            llegada = 5 * dato[0]
        elif tipo == "corto" and linea == dato[1]:
            llegada = 7 * dato[0]
    return llegada
def llegadadetren(horatrenes, tipo, listadelineas, linea):
    tllegada = tiempodellegada(tipo, linea, listadelineas)
    



    
def proximos_trenes(estaciones, tipos, trenes, estacion, hora):
    for lineas in listadelineas:
        lin.append([listadelineas.index(lineas)+1, lineas])
