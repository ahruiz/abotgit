#codigo para calcular el indice de masa corporal

print("-" * 90)
print("Calcular IMC de acuerdo al peso y la estatura")

peso = float(input("introduce tu peso en Kgs: "))
estatura = float(input("introduce tu estatura en metros: "))

imc = round(peso / (estatura*estatura),2)
print("-" * 90)

print(f"En base a tu peso {peso} y tu estatura {estatura} tienes un IMC de {imc}")

if imc <= 18.5:
    print(f"Un IMC menor 18.5 se considera : BAJO PESO....DEBES ALIMENTARTE MEJOR!!!")
elif imc > 18.5 and imc < 24.9:
    print(f"Un IMC entre 18.5 y 24.9 se considera : PESO NORMAL...UN BUEN PESO ES UNA BUENA SALUD!!!")
elif imc > 25.0 and imc < 29.9:
    print(f"Un IMC entre 25.0 y 29.9 se considera : SOBREPESO....CUIDADO CON TUS HABITOS ALIMENTICIOS")
elif imc > 30.0 and imc < 34.9:
    print(f"Un IMC entre 30.0 y 34.9 se considera : OBESIDAD tipo I.....ALERTAAA, COME MENOS Y EJERCITATE MAS")
elif imc > 35.0 and imc < 39.9:
    print(f"Un IMC entre 35.0 y 39.9 se considera : OBESIDAD tipo II....ES NECESARIO ACUDIR AL NUTRIOLOGO")
else:
    print(f"Un IMC mayor a 40.0 se considera : OBESIDAD tipo III....PELIGROOOO, TU SALUD ESTA EN RIESGO")


print("-" * 90)
