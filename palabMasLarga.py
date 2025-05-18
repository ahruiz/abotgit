#codigo para determinar la pañabra mas larga de un texto
#ingresado por ek usuario

print("-" * 80)
print("------- Codigo para determinar la palabra mas larga de un texto -------")

mitexto = input("Ingresa el TEXTO a analizar....: ")

palabras = mitexto.split()

longTxt = len(palabras)

longMasLarga = max(len(palabra) for palabra in palabras)
palMasLarga = {palabra for palabra in palabras if len(palabra) == longMasLarga} #porque con parentesis no jala

#print(f" mi texto es : {palabras} con {longTxt} palabras")
print(f"la palabra mas larga es {palMasLarga} con una longitud de {longMasLarga}")
print("-" * 80)