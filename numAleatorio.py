import random

# generamos un num aleatorio entre 1 y 10 y se guarda en 

print("-" * 60)
print("***proceso generador de numero escondido aleatorio entre 1 y 10***")
hidenNum=random.randint(1, 10)

while True:
    numero = input("escribe el numero que piensas que se generó: ")

    if  not numero.isdigit():
        print("debes ingresar un numero, no caracteres diferentes")
        continue 
    numero = int(numero)
    if numero < 1 or numero > 10 :
        print("Debes teclear numeros del 1 al 10")
        continue
    if numero < hidenNum or numero > hidenNum:
        print("Mala suerte!!! Intentalo de nuevo!!!")
    else:
        print(f"FELICIDADES.....ganaste un cupon!!!!!")
        print("-" * 60)
        break
