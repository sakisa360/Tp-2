descripcion_artefacto = input("Describa el artefacto que ha encontrado: ")

es_tesoro = False

if "dorado" in descripcion_artefacto or "brillante" in descripcion_artefacto or "gema" in descripcion_artefacto:
  es_tesoro = True

if es_tesoro:
  mensaje = "¡Felicidades! Parece que has encontrado un tesoro oculto."
else:
  mensaje = "Este artefacto parece ser solo una decoración."

print(mensaje)
