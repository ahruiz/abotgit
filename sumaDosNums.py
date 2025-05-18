#Codigo para pedir 2 numeros, sumarlos y mostrarlos

print("-" * 80)
print("Codigo para pedir dos numeros al usuario y sumarlos ")

numeros = []
cantNums = 2

for i in range(cantNums):
    num = int(input(f"ingresa el numero {i + 1}: ")) #se solicita el numero por ciclo
    numeros.append(num)                              # y se guarda en el diccionario hasta completar el ciclo del for
                                                     
totSuma = sum(numeros)

print(f"los numeros capturados son: {numeros}")
print(f"La suma de esos numeros es: {totSuma}")
print("-" * 80)