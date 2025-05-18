#codigo para determinar el promedio de calificaciones
#capturadas por el usuario
print("-" * 80)
totCalif = int(input("cuantas calificaciones quieres capturar: "))

calif = []

for i in range(totCalif):
    micalif = int(input(f"ingrese la calificacion {i + 1}:  "))
    calif.append(micalif)

prom = sum(calif) / len(calif)
print(calif)
print(f"El promedio de mis calificaciones es: {prom}")
print("-" * 80)

