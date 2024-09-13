print("Funciones version 2")
print("Andres Rivera")
#zona de listas, tuplas, sets y diccionarios
jugadores = ["Messi", "CR7", "Neymar"]
comida = ("Tacos", "Pozole", "Mole")
marcasPc = {"Logitech", "Xpg", "Razer"}
carros = {
  "Marca :": "Chevrolet",
  "Modelo : ": "Camaro",
  "Año :": 1969
}

#zona de funciones
def verlista(goats):
  for unjugador in goats:
    print(unjugador)

def vertupla(food):
  for unaComida in food:
    print(unaComida)

def versets(pc):
  for unamarca in pc:
    print(unamarca)

def verdiccionarios(vehiculo):
  for uncarro, otrocarro in vehiculo.items():
    print(uncarro, otrocarro)


#Llamada de funciones
print("Imprime jugadores de una lista")
verlista(jugadores)
print("Imprime comida de una tupla")
vertupla(comida)
print("Imprime marcas de pc de un set")
versets(marcasPc)
print("Imprime carro de un diccionario")
verdiccionarios(carros)

