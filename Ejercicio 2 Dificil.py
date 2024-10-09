def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

numero_personajes = int(input("¿Cuántos personajes hay en total? "))

# Cálculo del número de combinaciones
combinaciones = factorial(numero_personajes) // factorial(numero_personajes - 3) // factorial(3)

mensaje = f"¡En este mundo mágico, puedes formar hasta {combinaciones} equipos de aventureros diferentes!"

print(mensaje)
