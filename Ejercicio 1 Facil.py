def calcular_tiempo_a_la_luna(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo
distancia_tierra_luna = float(input("Ingresa la distancia entre la Tierra y la Luna (en km): "))
velocidad_nave = float(input("Ingresa la velocidad de la nave espacial (en km/s): "))
tiempo_viaje = calcular_tiempo_a_la_luna(distancia_tierra_luna, velocidad_nave)
print("El tiempo de viaje a la Luna es:", tiempo_viaje, "horas")
