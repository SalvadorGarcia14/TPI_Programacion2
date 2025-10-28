from habilidad import Habilidad
from raza import Raza
from bando import Bando
from clase_de_personaje import ClaseDePersonaje


from typing import List


#Creando Bnados

alianza = Bando("Alianza")
horda = Bando("Horda")

#Creando Razas

#razas Alianza
humano = Raza("Humano", alianza, ["Guerrero","Cazador", "Mago", "Paladin"])
elfo_de_la_noche = Raza("Elfo de la Noche", alianza, ["Guerrero","Cazador", "Druida"])

#Razas Horda
orco = Raza("Orco", horda, ["Guerrero","Cazador", "Mago", "Chaman"])
no_muerto = Raza("No Muerto", horda, ["Guerrero","Cazador", "Brujo"])

#Creando Habilidades

#Habilidades Guerrero
golpe_de_escudo = Habilidad("Golpe de Escudo", "Física", 20, 30)
carga = Habilidad("Carga", "Física", 15, 10)
tormenta_de_espadas = Habilidad("Tormenta de Espadas", "Física", 40, 50)

#Habilidades Cazador
triple_disparo = Habilidad("Triple Disparo", "Física", 25, 35)
maldicion_de_sangre = Habilidad("Maldición de Sangre", "Oscura", 30, 40)
disparo_aturdidor = Habilidad("Disparo Aturdidor", "Física", 10, 5)

#Habilidades Mago
bola_de_fuego = Habilidad("Bola de Fuego", "Fuego", 30, 45)
rayo_de_hielo = Habilidad("Rayo de Hielo", "Hielo", 25, 35)
escudo_de_mana = Habilidad("Escudo de Mana", "Arcano", 20, 0)

#habilidades Paladin
luz_sagrada = Habilidad("Luz Sagrada", "Sagrado", 20, 30) 
martillo_de_justicia = Habilidad("Martillo de Justicia", "Sagrado", 15, 20)
bendicion_de_proteccion = Habilidad("Bendición de Protección", "Sagrado", 25, 0)

#Habilidades Druida
forma_felina = Habilidad("Forma Felina", "Natural", 20, 0)
embate = Habilidad("Embate", "Física", 15, 25)  
fuerza_de_la_naturaleza = Habilidad("Fuerza de la Naturaleza", "Natural", 30, 40)

#Habilidades Chamán
onda_de_tormenta = Habilidad("Onda de Tormenta", "Elemental", 25, 35)
cadenas_de_relampago = Habilidad("Cadenas de Relámpago", "Elemental", 30, 40)
totem_de_vida = Habilidad("Tótem de Vida", "Elemental", 20, 0)

#Habilidades Brujo
drenar_vida = Habilidad("Drenar Vida", "Oscura", 20, 30)
explosion_de_fuego = Habilidad("Explosión de Fuego", "Fuego", 25, 35)
invocar_demonio = Habilidad("Invocar Demonio", "Oscura", 30, 0)

#Creando Clases de Personaje

paladin_humano = ClaseDePersonaje("Paladín Humano", "Tank-DPS", 110, humano, [luz_sagrada, martillo_de_justicia, bendicion_de_proteccion])
guerrero_orco = ClaseDePersonaje("Guerrero Orco", "Tank", 120, orco, [golpe_de_escudo, carga, tormenta_de_espadas])
brujo_no_muerto = ClaseDePersonaje("Mago No Muerto", "DPS", 100, no_muerto, [drenar_vida, explosion_de_fuego, invocar_demonio])
cazador_elfo = ClaseDePersonaje("Cazador Elfo de la Noche", "DPS", 105, elfo_de_la_noche, [triple_disparo, maldicion_de_sangre, disparo_aturdidor])
























#Exportando datos
datos_bandos = [alianza, horda]

datos_razas = [humano, elfo_de_la_noche, orco, no_muerto]

datos_clases = [paladin_humano, guerrero_orco, brujo_no_muerto, cazador_elfo]

datos_habilidades = [golpe_de_escudo, carga, tormenta_de_espadas, triple_disparo, maldicion_de_sangre, disparo_aturdidor,
                    bola_de_fuego, rayo_de_hielo, escudo_de_mana, luz_sagrada, martillo_de_justicia, bendicion_de_proteccion,
                    forma_felina, embate, fuerza_de_la_naturaleza, onda_de_tormenta, cadenas_de_relampago, totem_de_vida,
                    drenar_vida, explosion_de_fuego, invocar_demonio]







#Ejemplos de uso (descomentar para probar)

for bando in datos_bandos:
    print(bando)
    
for raza in datos_razas:
    print(raza)

for clase in datos_clases:
    print(clase)

for habilidad in datos_habilidades:
    print(habilidad)
    

print(brujo_no_muerto)
print(f"Total de clases creadas: {ClaseDePersonaje.cantidadClases()}")