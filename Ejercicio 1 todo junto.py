import math
def calcular_tiempo_a_la_luna(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo
def calcular_area_superficie(base, altura):
    area = base * altura
    return area

def calcular_combinaciones(total_personas, tamano_equipo):
    combinaciones = math.comb(total_personas, tamano_equipo)
    return combinaciones
distancia_tierra_luna = float(input("Ingresa la distancia entre la Tierra y la Luna (en km): "))
velocidad_nave = float(input("Ingresa la velocidad de la nave espacial (en km/s): "))
tiempo_viaje = calcular_tiempo_a_la_luna(distancia_tierra_luna, velocidad_nave)
base_superficie = float(input("Ingresa la base de la superficie lunar (en km): "))
altura_superficie = float(input("Ingresa la altura de la superficie lunar (en km): "))
area_superficie = calcular_area_superficie(base_superficie, altura_superficie)
total_personas = int(input("Ingresa el número total de personas disponibles: "))
tamano_equipo = int(input("Ingresa el tamaño del equipo deseado: "))
num_combinaciones = calcular_combinaciones(total_personas, tamano_equipo)
print("El tiempo de viaje a la Luna es:", tiempo_viaje, "horas")
print("El área de la superficie lunar es:", area_superficie, "kilómetros cuadrados")
print("El número total de combinaciones posibles de equipos de astronautas es:", num_combinaciones)