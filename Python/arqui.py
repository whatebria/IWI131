NumeroBinario = input("Ingrese su numero binario: ")

resultado = 0
contador = 0

for numero in reversed(NumeroBinario):
    if numero == "1":
        resultado += (2**contador) * 1
    else:
        resultado += (2**contador) * 0
    contador += 1

print("Su numero en decimal es: ", resultado)