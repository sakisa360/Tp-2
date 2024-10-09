def hechizo_suficientemente_fuerte(potencia_hechizo, resistencia_enemigo):
    return potencia_hechizo > resistencia_enemigo
# Solicitar al usuario que ingrese la potencia del hechizo y la resistencia del enemigo
potencia_hechizo = float(input("Ingresa la potencia del hechizo: "))
resistencia_enemigo = float(input("Ingresa el nivel de resistencia del enemigo: "))
# Verificar si el hechizo es lo suficientemente fuerte para derrotar al enemigo
if hechizo_suficientemente_fuerte(potencia_hechizo, resistencia_enemigo):
    print("¡El hechizo es lo suficientemente fuerte para derrotar al enemigo!")
else:
    print("El hechizo no es lo suficientemente fuerte para derrotar al enemigo.")
