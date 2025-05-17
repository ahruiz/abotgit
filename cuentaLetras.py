#codigo para contar las letras de una palabra
print("-" * 80)
print("Vamos a contar las letras de una o varias palabras dadas por el usuario")


texto = input("Introduce un texto o una palabra: ")
txtsinespacio = texto.replace(" ","") #eliminamos los espacios

longPal = len(txtsinespacio)

print(f"El texto es: [{texto}] y tiene una longitud de {longPal} ")
print("-" * 80)
