import random

def generar_pregunta():
  preguntas = [
    "¿Cuál es la criatura mágica con alas de fuego?",
    "¿En qué ciudad se encuentra la Fuente de la Eterna Juventud?",
    "¿Quién forjó el poderoso anillo mágico llamado 'El Ojo de Sauron'?"
  ]
  pregunta_aleatoria = random.choice(preguntas)
  return pregunta_aleatoria

def verificar_respuesta(pregunta, respuesta):
  if pregunta == "¿Cuál es la criatura mágica con alas de fuego?":
    return respuesta.lower() == "dragon"
  elif pregunta == "¿En qué ciudad se encuentra la Fuente de la Eterna Juventud?":
    return respuesta.lower() == "el dorado"
  elif pregunta == "¿Quién forjó el poderoso anillo mágico llamado 'El Ojo de Sauron'?":
    return respuesta.lower() == "sauron"
  else:
    return False

num_preguntas_correctas = 0

while num_preguntas_correctas < 3:
  pregunta = generar_pregunta()
  print(pregunta)
  respuesta_usuario = input("Ingrese su respuesta: ")

  if verificar_respuesta(pregunta, respuesta_usuario):
    print("¡Correcto!")
    num_preguntas_correctas += 1
  else:
    print("Respuesta incorrecta. Inténtalo de nuevo.")

if num
