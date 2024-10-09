mensaje_estatua = input("Ingrese el mensaje grabado en la estatua: ")

es_pista = False

if "mapa" in mensaje_estatua or "brújula" in mensaje_estatua or "secreto" in mensaje_estatua:
  es_pista = True

if es_pista:
  mensaje = "¡Este mensaje podría ser una pista valiosa para encontrar el tesoro!"
else:
  mensaje = "Parece que este mensaje es solo una distracción."

print(mensaje)
