#Codigo para pedir 2 numeros, sumarlos y mostrarlos

print("-" * 80)
print("Codigo para pedir dos numeros al usuario y restar el 2do del 1ro ")

numeros = []
cantNums = 2

for i in range(cantNums):
    num = int(input(f"ingresa el numero {i + 1}: ")) #se solicita el numero por ciclo
    numeros.append(num)                              # y se guarda en el diccionario hasta completar el ciclo del for
                                                     
totResta = numeros[1] - numeros[0]

if totResta < 0:
    print(f"Los numeros capturados son {numeros} y su resta es {totResta} y es NEGATIVO")
elif totResta > 0:  
    print(f"Los numeros capturados son {numeros} y su resta es {totResta} y es POSITIVO")
else:
    print(f"Los numeros capturados son {numeros} y su resta es {totResta} y es CERO")

print("-" * 80)