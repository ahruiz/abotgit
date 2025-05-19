#codigo para diferenciar peliculas de acuerdo a la edad

print("-" * 80)
print("Mostrar peliculas de acuerdo a la edad")

peliculas = {'A':'EL ARO', 'B':'PINOCHO', 'C':'EL EXORCISTA', 'D':'LOS VENGADORES' }
edad = int(input("Indicanos que edad tienes: "))

pelicPermitidas = peliculas.get('B') + ' y ' + peliculas.get('D')
pelicNopermitidas = peliculas.get('A') + ' Y ' + peliculas.get('C')

if edad < 18:
    
    print(f"Las peliculas permitidas son: {pelicPermitidas}")
if edad > 18:
    print(f" Las peliculas PERMITIDAS son: {pelicPermitidas} ademas de {pelicNopermitidas}")

print("-" * 80)