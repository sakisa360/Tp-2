def calcular_area_superficie(base, altura):
    area = base * altura
    return area
base_superficie = float(input("Ingresa la base de la superficie lunar (en km): "))
altura_superficie = float(input("Ingresa la altura de la superficie lunar (en km): "))
area_superficie = calcular_area_superficie(base_superficie, altura_superficie)
print("El área de la superficie lunar es:", area_superficie, "kilómetros cuadrados")
