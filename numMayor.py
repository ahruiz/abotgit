#codigo para identificar el numero mayor de una lista

print("-" * 80)
print("identificar el numerpo mas alto de una lista dada")

#lista = [-10,-1,0,-12,-13,-5,-17,-33,-87,-99]
cantNums = int(input("cuantos numeros quieres capturar: "))

misNums = []

for i in range(cantNums):
    nums = int(input(f"Ingresa el numero {i +1}: "))
    misNums.append(nums)

nummay = max(misNums)
print(f"Mi lista de numeros es: {misNums}")
print(f"El numero mayor en mi lista es : {nummay}")
print("-" * 80)