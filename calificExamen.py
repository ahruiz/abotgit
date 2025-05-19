#codigo para calificar examenes en base a datos
#proporcionados por el usuario
print("-" * 90)
print("Captura los datos para calificar tu examen.....")

totPreguntas = input("indica el total de preguntas del examen: ")
aciertos = input("indica el total de aciertos del examen: ")
fallos  = input("indica el total de fallos del examen: ")

if not totPreguntas.isdigit() or not aciertos.isdigit() or not fallos.isdigit():
    print("Debes capturar valores numericos enteros y no otro tipo de caracteres")
    exit()

aciertos = int(aciertos)
totPreguntas = int(totPreguntas)

calif = round((aciertos / totPreguntas) * 100,2)

print(f"**************************************** Mi calificacion   : {calif}")

print("-" * 90)