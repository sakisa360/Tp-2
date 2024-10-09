import math
def calcular_combinaciones(total_personas, tamano_equipo):
    combinaciones = math.comb(total_personas, tamano_equipo)
    return combinaciones
total_personas = int(input("Ingresa el número total de personas disponibles: "))
tamano_equipo = int(input("Ingresa el tamaño del equipo deseado: "))
num_combinaciones = calcular_combinaciones(total_personas, tamano_equipo)
print("El número total de combinaciones posibles de equipos de astronautas es:", num_combinaciones)
