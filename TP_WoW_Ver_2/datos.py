# ===============================================
# Datos precargados del juego "WORLD OF PYTHONCRAFT v1.0"
# Contiene las instancias iniciales de Habilidades, Clases, Razas,
# Jugadores, Enemigos, Objetos e Inventarios.
# ===============================================


from habilidad import Habilidad
from clase_personaje import ClasePersonaje
from bando import Bando
from raza import Raza
from jugador import Jugador
from enemigo import Enemigo
from objeto import Objeto
from inventario import Inventario


#Bandos
alianza = Bando("Alianza")
horda = Bando("Horda")

# Habilidades

#Habilidad General Ataque Basico
ataque_basico = Habilidad("Ataque Básico", "Física", 0, 10)

#Habilidad Ataque Basico de Guerrero
ataque_basico_guerrero = Habilidad("Ataque Básico Guerrero", "Física", 0, 10)

#Habilidad Ataque Basico de mago
ataque_basico_mago = Habilidad("Ataque Básico Mago", "Física", 0, 5)

#Habilidad Ataque Basico de Cazador
ataque_basico_cazador = Habilidad("Ataque Básico Cazador", "Física", 0, 13)

#Habilidad Ataque Basico de Druida
ataque_basico_druida = Habilidad("Ataque Básico Druida", "Física", 0, 8)

#Habilidad Ataque Basico de Paladin
ataque_basico_paladin = Habilidad("Ataque Básico Paladín", "Física", 0, 12)

#Habilidad Ataque Basico de Brujo
ataque_basico_brujo = Habilidad("Ataque Básico Brujo", "Física", 0, 5)

#Hbailidades Ataque Basico de Chaman
ataque_basico_chaman = Habilidad("Ataque Básico Chamán", "Física", 0, 8)




#habilidades Guerrero
golpe_de_escudo = Habilidad("Golpe de Escudo", "Física", 20, 30)
carga = Habilidad("Carga", "Física", 15, 10)
tormenta_de_espadas = Habilidad("Tormenta de Espadas", "Física", 40, 50)

#Habilidades Mago
bola_de_fuego = Habilidad("Bola de Fuego", "Fuego", 25, 30)
rayo_de_hielo = Habilidad("Rayo de Hielo", "Hielo", 20, 25)
tormenta_de_escarcha = Habilidad("Tormenta de Escarcha", "Hielo", 35, 40)

#Habilidades Cazador
disparo_letal = Habilidad("Disparo Letal", "Física", 30, 20)
trampa_explosiva = Habilidad("Trampa Explosiva", "Física", 20, 15)
lluvia_de_flechas = Habilidad("Lluvia de Flechas", "Física", 40, 35)

#Habilidades Druida
forma_de_felina = Habilidad("Forma de Felina", "Física", 10, 0)
raices_enredadoras = Habilidad("Raíces Enredadoras", "Naturaleza", 20, 15)
tormenta_silvestre = Habilidad("Tormenta Silvestre", "Naturaleza", 35, 30)

#Habilidades Paladin
martillo_de_justicia = Habilidad("Martillo de Justicia", "Sagrado", 25, 20)
aura_de_proteccion = Habilidad("Aura de Protección", "Sagrado", 0, 15)
golpe_consecrado = Habilidad("Golpe Consagrado", "Sagrado", 35, 30)

#Habilidades Brujo
drenar_vida = Habilidad("Drenar Vida", "Sombras", 20, 25)
explosion_de_los_infernos = Habilidad("Explosión de los Infernos", "Fuego", 30, 35)
invocar_demonio = Habilidad("Invocar Demonio", "Sombras", 10, 40)

#Habilidades Chaman
onda_de_tormenta = Habilidad("Onda de Tormenta", "Elemental", 25, 30)
escudo_de_tierra = Habilidad("Escudo de Tierra", "Elemental", 0, 20)
tomen_de_vida = Habilidad("Tótem de Vida", "Elemental", 15, 0)


#Lista de todas las habilidades
habilidades = [
    ataque_basico,
    ataque_basico_guerrero,
    ataque_basico_mago,
    ataque_basico_cazador,
    ataque_basico_druida,
    ataque_basico_paladin,
    ataque_basico_brujo,
    ataque_basico_chaman,
    golpe_de_escudo,
    carga,
    tormenta_de_espadas,
    bola_de_fuego,
    rayo_de_hielo,
    tormenta_de_escarcha,
    disparo_letal,
    trampa_explosiva,
    lluvia_de_flechas,
    forma_de_felina,
    raices_enredadoras,
    tormenta_silvestre,
    martillo_de_justicia,
    aura_de_proteccion,
    golpe_consecrado,
    drenar_vida,
    explosion_de_los_infernos,
    invocar_demonio,
    onda_de_tormenta,
    escudo_de_tierra,
    tomen_de_vida
]



# Clases de Personaje
guerrero = ClasePersonaje("Guerrero", "Tank", 15, [ataque_basico_guerrero, golpe_de_escudo, carga, tormenta_de_espadas])
mago = ClasePersonaje("Mago", "DPS", 10, [ataque_basico_mago, bola_de_fuego, rayo_de_hielo, tormenta_de_escarcha])
cazador = ClasePersonaje("Cazador", "DPS", 12, [ataque_basico_cazador, disparo_letal, trampa_explosiva, lluvia_de_flechas])
druida = ClasePersonaje("Druida", "Healer", 11, [ataque_basico_druida, forma_de_felina, raices_enredadoras, tormenta_silvestre])
paladin = ClasePersonaje("Paladín", "Tank", 14, [ataque_basico_paladin, martillo_de_justicia, aura_de_proteccion, golpe_consecrado])
brujo = ClasePersonaje("Brujo", "DPS", 9, [ataque_basico_brujo, drenar_vida, explosion_de_los_infernos, invocar_demonio])
chaman = ClasePersonaje("Chamán", "Healer", 11, [ataque_basico_chaman, onda_de_tormenta, escudo_de_tierra, tomen_de_vida])

#Lista de Clases de Personaje
clases_personaje = [
    guerrero,
    mago,
    cazador,
    druida,
    paladin,
    brujo,
    chaman
]   


# Razas

#Alianza
humano = Raza("Humano", alianza, [guerrero, mago, cazador, paladin])
elfo_noche = Raza("Elfo de la Noche", alianza, [guerrero, druida, cazador, mago])

#Horda
orco = Raza("Orco", horda, [guerrero, cazador, mago, chaman])
No_Muerto = Raza("No-Muerto", horda, [guerrero, cazador, brujo])


#Lista de Razas
razas = [
    humano,
    elfo_noche,
    orco,
    No_Muerto
]

#Objetos y Inventarios
espada = Objeto(
    nombre="Espada Rúnica",
    descripcion="Una espada forjada con runas antiguas que aumenta el ataque.",
    tipo="equipable",
    efectos={"ataque": 10},   # +10 de ataque
    valor=100
)

arco = Objeto(
    nombre="Arco Largo",
    descripcion="Ideal para combates a distancia, aumenta ligeramente el ataque.",
    tipo="equipable",
    efectos={"ataque": 8},    # +8 de ataque
    valor=90
)

pocion = Objeto(
    nombre="Poción de Curación",
    descripcion="Restaura puntos de vida al usarse.",
    tipo="consumible",
    efectos={"vida": 25},     # +25 HP (sin superar vida máxima)
    valor=20
)

talisman = Objeto(
    nombre="Talismán Sombrío",
    descripcion="Aumenta la vida máxima del portador.",
    tipo="equipable",
    efectos={"vida_max": 60},  # +60 vida máxima
    valor=150
)

objetos = [
    espada,
    arco,
    pocion,
    talisman
]


# Inventarios individuales

inventario_salvi = Inventario(oro=100, objetos=[])
inventario_salvi.agregar_objeto(pocion)
inventario_salvi.agregar_objeto(pocion)
inventario_salvi.agregar_objeto(pocion)
inventario_salvi.agregar_objeto(pocion)
inventario_salvi.agregar_objeto(arco)
inventario_salvi.agregar_objeto(talisman)

inventario_jorjito = Inventario(oro=150, objetos=[])
inventario_jorjito.agregar_objeto(espada)
inventario_jorjito.agregar_objeto(talisman)


# Jugadores Precargados
ShadoWSalvi = Jugador(
    nombre="ShadoWSalvi",
    nivel=1,
    salud=100,
    salud_maxima= 100,
    mana=80,
    mana_maxima=80,
    clase_personaje=cazador,
    inventario=inventario_salvi,
    nombre_usuario="ShadowUser",
    experiencia=0,
    defensa=15,
    ataque= 15
)

Jorjito = Jugador(
    nombre="Jorjito",
    nivel=1,
    salud=120,
    salud_maxima=120,
    mana=60,
    mana_maxima=60,
    clase_personaje=paladin,
    inventario=inventario_jorjito,
    nombre_usuario="JorjitoPal",
    experiencia=0,
    defensa=20,
    ataque= 10
)

#Lista de jugadores 
jugadores = [
    ShadoWSalvi,
    Jorjito
]


#Enemigos Precargados


#Habilidades Enemigas

#Habilidad de Lobo Feroz
mordida = Habilidad("Mordida", "Física", 5, 10) #0
zarpa = Habilidad("Zarpazo", "Fisica", 10, 12)#1
salgo_zarpa = Habilidad("Salto Zarpa", "Fisica" ,5, 6)#2

#Habilidad de Troll del Bosque
lanzar_hacha = Habilidad("Lanzar Hacha", "Física", 10, 20) #3
aturdir = Habilidad("Aturdir", "Física", 10, 10) #4
ataque_multiple = Habilidad("Ataques Multiples", "Fisica", 15, 25) #5

#Habilidad Nigromante
miedo = Habilidad("Lanzar Miedo","Sombras", 5, 10) #6
levantar_muertos = Habilidad("Levantar Muertos", "Sombras", 10, 15) #7
explosion_vil = Habilidad("Explocion Oscura", "Sombras", 20, 40) #8

#Habilidad Dragon Rojo
vuelo_poderoso = Habilidad("Vuelo Poderoso", "Fisica", 10, 20)
aliento_fuego = Habilidad("Aliento de Fuego Destructivo", "Elemental", 20, 60)
aliento_final = Habilidad("Aliento de Fuego Final", "Elemental", 30, 90)

#Agregar habilidades

habilidades_enemigas = [
    
]
#Lobo Feroz
habilidades_enemigas.append(mordida) #0
habilidades_enemigas.append(zarpa) #1
habilidades_enemigas.append(salgo_zarpa) #2

#Troll del Bosque
habilidades_enemigas.append(lanzar_hacha) #3
habilidades_enemigas.append(aturdir) #4
habilidades_enemigas.append(ataque_multiple) #5

#Nigromante
habilidades_enemigas.append(miedo) #6
habilidades_enemigas.append(levantar_muertos) #7
habilidades_enemigas.append(explosion_vil) #8

#Dragon Rojo
habilidades_enemigas.append(vuelo_poderoso) #9
habilidades_enemigas.append(aliento_fuego) #10
habilidades_enemigas.append(aliento_final) #11

#Clase Enemigos

guerrero_enemigo_lobo = ClasePersonaje("Guerrero Lobo Feroz", "Taks", 15, habilidades_enemigas[0: 3])
guerrero_troll_del_bosque = ClasePersonaje("Guerrero Troll Del Bosque", "DPS", 20, habilidades_enemigas[3: 6])
mago_nigromante = ClasePersonaje("Nigromante", "DPS", 20, habilidades_enemigas[6 : 9])
dragon_rojo_unico = ClasePersonaje("Dragon Rojo", "DPS/Tank", 20,habilidades_enemigas[9: 12] )


# Enemigos Precargados
lobo_feroz = Enemigo(
    nombre="Lobo Feroz",
    nivel=5,
    salud=20,
    salud_maxima=20,
    mana=30,
    mana_maxima=30,
    clase_personaje=guerrero_enemigo_lobo, 
    inventario=Inventario(oro=0, objetos=[]),
    tipo_enemigo="común",
    recompensa_experiencia=50,
    rango_oro=[5,10]
)

trol_bosque = Enemigo(
    nombre="Trol del Bosque",
    nivel=7,
    salud=70,
    salud_maxima=70,
    mana=50,
    mana_maxima=50,
    clase_personaje=guerrero_troll_del_bosque,
    inventario=Inventario(oro=0, objetos=[]),
    tipo_enemigo="raro",
    recompensa_experiencia=80,
    rango_oro=[15,30]
)

nigromante = Enemigo(
    nombre="Nigromante Oscuro",
    nivel=10,
    salud=100,
    salud_maxima=100,
    mana=100,
    mana_maxima=100,
    clase_personaje=mago_nigromante,
    inventario=Inventario(oro=0, objetos=[]),
    tipo_enemigo="épico",
    recompensa_experiencia=150,
    rango_oro=[50,60]
)

dragon_rojo = Enemigo(
    nombre="Dragon Rojo", 
    nivel=20,
    salud=400,
    salud_maxima=400,
    mana=300,
    mana_maxima=300,
    clase_personaje=dragon_rojo_unico,
    inventario=Inventario(oro=50, objetos=[]),
    tipo_enemigo="legendario",
    recompensa_experiencia=100,
    rango_oro=[100,200]  
)

#Objetos de dragon
objeto_huevo_dragon = Objeto(
    nombre="Huevo de Dragon Rojo",
    descripcion="Este es un objeto unico de Dragon",
    tipo=None, #No se equipa
    efectos=None, #No tiene efecto
    valor= 500
    
)

inventario_salvi.agregar_objeto(objeto_huevo_dragon)


enemigos = [
    lobo_feroz,
    trol_bosque,
    nigromante,
    dragon_rojo
]

"""
    
for enemigo in enemigos:
    print(enemigo)

"""


#Agrupacion global de los datos precargados
def obtener_datos_precargados(): #Devuelve todas las colecciones del juego.
    return {
        "habilidades": habilidades,
        "clases_personaje": clases_personaje,
        "razas": razas,
        "jugadores": jugadores,
        "enemigos": enemigos,
        "objetos": [espada, arco, pocion, talisman]
    }

 
# ====================================================

#=================== TEST ===========================


"""


print("=" * 20)
#Crosover 

clases_pokemon = []

#Bando
pokemon = Bando("Pokemon")

#Razas
pokemon = Bando("Pokemon")

#Agregar nueva raza

pokemos = Raza("Pokemos", None, clases_pokemon)

pokemos.agregar_bando_a_la_raza(pokemon)

print(pokemos)



#habilidades 

inpactrueno = Habilidad("Inpactrueno", "Rayo", 10, 10)
curacion = Habilidad("Curacion", "healer", 5, 0)
salto_trueno = Habilidad("Salto Trueno", "esquivar", 5, 0)


habilidades_pokemon = [
    
]


tipo_electrico = ClasePersonaje("Tipo Electrico", "DPS",  10, habilidades_pokemon) 

tipo_electrico.agregar_habilidad(ataque_basico)
tipo_electrico.agregar_habilidad(inpactrueno)
tipo_electrico.agregar_habilidad(curacion)
tipo_electrico.agregar_habilidad(salto_trueno)

print(tipo_electrico)

print(tipo_electrico.obtener_habilidades())

inventario_pikachu = Inventario(oro=50, objetos=[])
pikachu = Jugador(
    nombre="Pikachu",
    nivel=1,
    salud=100,
    salud_maxima=100,
    mana=100,
    mana_maxima=100,
    clase_personaje=tipo_electrico,
    inventario=inventario_pikachu,
    nombre_usuario="PikachuUser",
    experiencia=0,
    defensa=10,
    ataque=10,
    nivel_maximo = 100,
)

pikachu.agregar_objeto_inventario(pocion)
pikachu.atacar(nigromante, habilidades[0])
print(pikachu.atacar(nigromante, habilidades[0]))

pikachu.recibir_daño(10)
print(pikachu.recibir_daño(10))
print(pikachu)

pikachu.mostrar_inventario()
print(pikachu.mostrar_inventario())


pikachu.ganar_experiencia(300)
print(pikachu.ganar_experiencia(300))

"""

