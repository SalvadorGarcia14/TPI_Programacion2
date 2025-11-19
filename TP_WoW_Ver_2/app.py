from datos import jugadores, enemigos, clases_personaje, razas, habilidades, objetos, alianza, horda

from inventario import Inventario
from jugador import Jugador

import random
import time


# Funciones auxiliares

def limpiar_pantalla():
    #Simula limpiar pantalla (para entorno consola simple).
    print("\n" * 3)

def pausar():
    input("\nPresiona Enter para continuar...")

# Funciones de visualización

def mostrar_jugadores():
    print("=== Lista de Jugadores ===\n")
   
    for jugador in jugadores: 
        print(f"{jugador}")



def mostrar_enemigos():
    print("=== Lista de Enemigos  ===\n")
    
    for enemigo in enemigos:
        print(enemigo)


def mostrar_clases():
    print("=== Clases Disponibles ===\n")
    for clase in clases_personaje:
        print(clase)
        
        

def mostrar_razas():
    print("=== Razas Disponibles ===\n")
    
    for raza in razas:
        print(raza)


def mostrar_objetos():
    print("=== Objetos ===\n")
    
    for objeto in objetos:
        print(objeto)
        
        
# ===============================================

# Combate


def submenu_combate(jugador_activo):
    while True:
        print(f"\n=== Modo Combate - {jugador_activo.nombre} ===")
        print("1. Buscar Enemigo Aleatorio")
        print("2. Ver Estado del Jugador")
        print("3. Usar Objeto")
        print("4. Volver al Menú Principal")
        
        opcion = input("Elige una opción: ")      

        if opcion == "1":
            enemigo = random.choice(enemigos)
            enemigo.resetear_salud()  # ✅ Resetea su salud antes de pelear
            enemigo.resetear_mana() 
            jugador_activo.resetear_mana()
            print(f"¡Has encontrado un {enemigo.nombre} de nivel {enemigo.nivel}!\n")
            combate(jugador_activo, enemigo)
            pausar()
        elif opcion == "2":
            print(jugador_activo)
            pausar()
        elif opcion == "3":
            seleccionar_objeto(jugador_activo)
        elif opcion == "4":
            print("Volviendo al menú principal...\n ")
            break
        else:
            print("Opción inválida. \n")
            pausar()


def combate(jugador_activo, enemigo):
    limpiar_pantalla()
    print(f"⚔️ ¡Combate iniciado entre {jugador_activo.nombre} y {enemigo.nombre}!\n")
    
    # Controla quién ataca
    turno_jugador = True 
    enemigo_vivo = True
    
    while jugador_activo.esta_vivo() and enemigo_vivo:
        print(f"\n{jugador_activo.nombre}: {jugador_activo.salud} HP | Daño Basico: {jugador_activo.ataque} |Mana: {jugador_activo.mana}")
        print(f"{enemigo.nombre}: {enemigo.salud} HP | Mana: {enemigo.mana}\n")
        
        if turno_jugador:
            print("=== Tu turno ===")
            print("1. Ataque básico")
            print("2. Usar habilidad")
            print("4. Huir del combate")

            opcion = input("Elige una acción: ")
            
            if opcion == "1":
                # Ataque básico, primera habilidad de las clases
                print("---Ataque Basico ---\n")
                habilidad_basica = jugador_activo.clase_personaje.habilidades[0]
                print(jugador_activo.atacar(enemigo, habilidad_basica))
            
            elif opcion == "2":
                print("--- Habilidades disponibles ---\n")
    
                # Mostrar solo las habilidades de la clase del jugador
                for i, habilidad in enumerate(jugador_activo.clase_personaje.habilidades):
                    print(f"{i + 1} - {habilidad}")
        
                eleccion = input("Elige habilidad: ")
                if eleccion.isdigit():
                    indice = int(eleccion) - 1
        
                    if 0 <= indice < len(jugador_activo.clase_personaje.habilidades):
                        habilidad = jugador_activo.clase_personaje.habilidades[indice]
                        resultado = jugador_activo.atacar(enemigo, habilidad)
                        print(resultado)
                    else:
                        print("Opción fuera de rango.")
                else:
                    print("Debes ingresar un número válido.")

            elif opcion == "4":
                print(f"{jugador_activo.nombre} huyó del combate ")
                return
            
            else:
                print("Opción inválida.")
                continue
            
            
            # Verificar si el enemigo murió
            if not enemigo.esta_vivo():
                print(f"{enemigo.nombre} ha sido derrotado. \n")
                enemigo_vivo = False

                exp, oro = enemigo.calcular_recompensa()
                print(jugador_activo.ganar_experiencia(exp))
                
                jugador_activo.inventario.modificar_oro(oro)
                print(f"Has ganado {oro} de oro!")
                
                # Drop aleatorio
                if objetos:
                    drop = random.choice(objetos)
                    print(f"El enemigo dejó caer un objeto: {drop.nombre}")
                    jugador_activo.agregar_objeto_inventario(drop)
                    break

            turno_jugador = False  # Ahora ataca el enemigo

        else:
            # Turno del enemigo
            print(f"=== Turno de {enemigo.nombre} === \n")
            habilidad_enemiga = random.choice(enemigo.clase_personaje.habilidades)
            print(enemigo.atacar(jugador_activo, habilidad_enemiga))

            if not jugador_activo.esta_vivo():
                print(f" {jugador_activo.nombre} ha muerto en combate. \n")
                pausar()
            if not jugador_activo.esta_vivo():
                print("Tu personaje ha muerto! \n")
                manejar_objetos_perdidos(jugador_activo)
                break

            turno_jugador = True
            time.sleep(1.5)

# Función para usar objetos
def seleccionar_objeto(jugador_activo):
    objetos = jugador_activo.inventario.objetos
    if not objetos:
        print("No tienes objetos para usar.")
        return
    
    while True:
        print("Objetos disponibles: \n")
        for i, objeto in enumerate(objetos, start=1):
            print(f"{i} -> {objeto}")

        print("0 -> Salir sin usar objeto")

        opcion = input("Elige un objeto: ")

        # Verifica si solo preciona ENTER o escribio algo no numerico
        if not opcion.isdigit():
            print(" Debes ingresar un número válido.")
            continue

        opcion = int(opcion)

        # 0 = salir
        if opcion == 0:
            print("Saliendo sin usar ningún objeto.")
            return

        # Vlida rango correcto
        if 1 <= opcion <= len(objetos):
            jugador_activo.inventario.usar_objeto(jugador_activo, opcion - 1)
            return
        else:
            print("Opción inválida, selecciona un número correcto \n")

            
# Función maneja la perdida de objetos del Inventario                
def manejar_objetos_perdidos(jugador_activo):
    inventario_original = jugador_activo.inventario.objetos.copy() # Guardamos una copia de seguridad del inventario

    jugador_activo.inventario.objetos.clear()
    print("Todos tus objetos se han perdido durante el combate... \n") # Vaciar inventario completamente

    while True:
        print("=== Objetos Perdidos === \n")
        print("1. Buscar los objetos perdidos")
        print("2. Seguir sin los objetos")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nBuscando objetos perdidos...")
            time.sleep(2)  # Simula búsqueda
            
            jugador_activo.inventario.objetos.clear()
            jugador_activo.inventario.objetos.extend(inventario_original)            
            print("¡Has encontrado todos tus objetos perdidos!")

            jugador_activo.salud = jugador_activo.salud_maxima
            jugador_activo.mana = jugador_activo.mana_maxima

            print("Tu personaje ha revivido completamente: \n")
            return

        elif opcion == "2":
            print("\nHas decidido seguir sin los objetos perdidos.")
            # --- REVIVIR AL JUGADOR ---
            jugador_activo.salud = jugador_activo.salud_maxima
            jugador_activo.mana = jugador_activo.mana_maxima

            print("Tu personaje ha revivido completamente: \n")
            return
        
        else:
            print("Opción incorrecta.")
        

                    
# ===============================================


def submenu_mercado(jugador_activo):

    while True:
        print("\n=== MERCADO ===")
        print(f"Oro disponible: {jugador_activo.inventario.oro}")
        print("Objetos en inventario:")

        objetos = jugador_activo.inventario.objetos

        if not objetos:
            print("No tienes objetos para vender.")
            input("Presiona ENTER para volver...")
            return

        for i, objeto in enumerate(objetos, start=1):
            print(f"[{i}] - {objeto.nombre} (Valor: {objeto.valor} oro)")

        print("0. Volver")
        
        opcion = input("Selecciona un objeto para vender: \n")

        if opcion == "0":
            return

        if not opcion.isdigit() or not (1 <= int(opcion) <= len(objetos)):
            print("Opción inválida.")
            continue

        objeto_seleccionado = objetos[int(opcion) - 1]
        confirmado = input(f"¿Quieres vender '{objeto_seleccionado.nombre}' por {objeto_seleccionado.valor} oro? (s/n): ").lower()
        if confirmado == "s":
            jugador_activo.inventario.oro += objeto_seleccionado.valor
            jugador_activo.inventario.objetos.remove(objeto_seleccionado)
            print(f"Vendiste {objeto_seleccionado.nombre} y recibiste {objeto_seleccionado.valor} oro.")
        else:
            print("Venta cancelada.")


# ===============================================



#Funciones Principal

def iniciar_sesion(): #Solicita el nombre de usuario y valida si existe en la lista de jugadores.
    print("======================================================================")
    print("      Bienvenido a WORLD OF PYTHONCRAFT  v1.2       ")
    print("======================================================================")
    print("Proyecto basado en POO y UML estilo WoW\n")

    while True:
        print("1 -> Iniciar Sesión")
        print("2 -> Nuevo Usuario")
        print("3 -> Salir\n")
        
        opcion = input("Elegi una opcion: ")
        
        if opcion == "1":

            nombre_usuario_ingresado = input("Ingrese su nombre de usuario: ")

            usuario_valido = None
            for jugador in jugadores:
                if jugador.nombre_usuario == nombre_usuario_ingresado:
                    usuario_valido = jugador
                    break

            if usuario_valido:
                print(f"Bienvenido {usuario_valido.nombre} ({usuario_valido.nombre_usuario}) \n")
                return usuario_valido
            else:
                print("Usuario no encontrado. Intente nuevamente. \n")
                continue
        elif opcion == "2":
            print("REGISTRO DE NUEVO USUARIO ")
            nuevo_usuario = input("Ingrese un nombre de usuario único: ").strip()
    
            if not nuevo_usuario:
                print("El nombre de usuario no puede estar vacío. \n")
                continue  # vuelve al menú
    
            # Verificar si el nombre ya existe
            existe = False
            for jugador in jugadores:
                if jugador.nombre_usuario == nuevo_usuario:  # <-- aquí era jugador.nombre, debería ser nombre_usuario
                    existe = True
                    break
    
            if existe:
                print("Ese nombre de usuario ya está en uso. Intenta con otro. \n")
                continue
    
            # Crear personaje automáticamente
            print(f"Usuario '{nuevo_usuario}' registrado con éxito. \n")
            pausar()
            nuevo_personaje = crear_nuevo_personaje(nuevo_usuario)
    
            if nuevo_personaje:
                print(f"¡Bienvenido {nuevo_personaje.nombre}! Tu aventura comienza ahora. \n")
                pausar()
                return nuevo_personaje
            else:
                print("No se pudo crear el personaje. Volviendo al menú principal. \n")
                continue


        elif opcion == "3":
            print("Saliendo del juego. ¡Hasta pronto!")
            return None

        else:
            print("Opción inválida. Intenta nuevamente.\n")

    
# def iniciar_sesion(): #Solicita el nombre de usuario y valida si existe en la lista de jugadores.
#     print("======================================================================")
#     print("      Bienvenido a WORLD OF PYTHONCRAFT  v1.0       ")
#     print("======================================================================")
#     print("Proyecto basado en POO y UML estilo WoW\n")
    
#     nombre_usuario_ingresado = input("Ingrese su nombre de usuario para iniciar sesión: ")
    
#     usuario_valido = None
#     for jugador in jugadores:
#         if jugador.nombre_usuario == nombre_usuario_ingresado:
#             usuario_valido = jugador
#             break
    
#     if usuario_valido:
#         print(f"\n✅ Bienvenido {usuario_valido.nombre} ({usuario_valido.nombre_usuario})\n")
#         return usuario_valido
#     else:
#         print("\n❌ Usuario no encontrado. Intente nuevamente.\n")
#         return None

#Seleccion de personaje
def seleccionar_personaje(jugadores, nombre_usuario):
    """Permite seleccionar un personaje entre los del usuario."""
    # Buscar el jugador por nombre de usuario
    personajes_usuario = []
    for jugador in jugadores:
        if jugador.nombre_usuario == nombre_usuario:
            personajes_usuario.append(jugador)

    if not personajes_usuario or len(personajes_usuario) == 0:
        print("❌ No tienes personajes creados aún.")
        return None

    print("=== SELECCIONAR PERSONAJE ===\n")
    for i, personaje in enumerate(personajes_usuario):
        print(f"{i + 1} - {personaje}")
        
    eleccion_str = input("\nElige el número de personaje: ")

    #Num entero
    if eleccion_str.isdigit():
        eleccion = int(eleccion_str) - 1
        if 0 <= eleccion < len(personajes_usuario):
            personaje_seleccionado = personajes_usuario[eleccion]
            print(f"\n✅ Has seleccionado a {personaje_seleccionado.nombre} "
                  f"({personaje_seleccionado.clase_personaje.nombre})\n")
            return personaje_seleccionado
        else:
            print("Opción fuera de rango. Volviendo al menú. \n")
            return None
    else:
        print("Entrada inválida. Debes ingresar un número. \n")
        return None


#Creacion de personaje
def crear_nuevo_personaje(nombre_usuario):
    limpiar_pantalla()
    print("=== CREACIÓN DE NUEVO PERSONAJE ===\n")
    
    print("Elige tu bando:")
    print("1 - Alianza")
    print("2 - Horda")
    opcion_bando = input("Opción: ")

    if opcion_bando == "1":
        bando_elegido = alianza
    elif opcion_bando == "2":
        bando_elegido = horda
    else:
        print("❌ Opción inválida.")
        return None

    limpiar_pantalla()
    print(f"Has elegido el bando: {bando_elegido.nombre}\n")

    # Filtra razas por bando
    razas_disponibles = []
    for raza in razas:
        if raza.bando == bando_elegido:
            razas_disponibles.append(raza)

    print("Elige tu raza:")
    for i, raza in enumerate(razas_disponibles):
        print(f"{i + 1} - {raza.nombre}")
    eleccion_raza = input("Opción: ")

    if not eleccion_raza.isdigit() or not (1 <= int(eleccion_raza) <= len(razas_disponibles)):
        print("❌ Opción inválida.")
        return None
    raza_elegida = razas_disponibles[int(eleccion_raza) - 1]
    limpiar_pantalla()
    print(f"Has elegido la raza: {raza_elegida.nombre}\n")
    
    
    print("Elige tu clase:")
    for i, clase in enumerate(raza_elegida.clases_disponibles):
        print(f"{i + 1} - {clase.nombre}")
    eleccion_clase = input("Opción: ")
    if not eleccion_clase.isdigit() or not (1 <= int(eleccion_clase) <= len(raza_elegida.clases_disponibles)):
        print("❌ Opción inválida.")
        return None
    clase_elegida = raza_elegida.clases_disponibles[int(eleccion_clase) - 1]
    limpiar_pantalla()
    print(f"Has elegido la clase: {clase_elegida.nombre}\n")
    
    nombre_personaje = input("Escribe el nombre de tu nuevo personaje: ").strip()
    if not nombre_personaje:
        print("❌ Nombre inválido.")
        return None
    
    nuevo_inventario = Inventario(oro=50, objetos=[])
    nuevo_personaje = Jugador(
        nombre=nombre_personaje,
        nivel=1,
        salud=100,
        salud_maxima=100,
        mana=80,
        mana_maxima=100,
        clase_personaje=clase_elegida,
        inventario=nuevo_inventario,
        nombre_usuario=nombre_usuario,
        experiencia=0,
        defensa=10,
        ataque=10,
    )
    
    
    jugadores.append(nuevo_personaje)
    print(f"\n✅ ¡Personaje '{nombre_personaje}' creado con éxito!")
    print(f"Bando: {bando_elegido} | Raza: {raza_elegida.nombre} | Clase: {clase_elegida.nombre}")
    print("Podrás seleccionarlo desde la opción 7 -> Seleccionar Personaje.")

    pausar()
    return nuevo_personaje





#menú principal
def main(): 
    jugador_activo = iniciar_sesion()

    if not jugador_activo:
        print("No se pudo iniciar sesión.")
        return

    while True:
        limpiar_pantalla()
        print(f"=== WORLD OF PYTHONCRAFT v1.2 ===")
        print(f"Jugador: {jugador_activo.nombre} | Nivel {jugador_activo.nivel}")
        print(f"Usuario: {jugador_activo.nombre_usuario} | Clase: {jugador_activo.clase_personaje.nombre}\n")
        print("1 -> Iniciar Combate \n")
        print("2 -> Mercado \n")
        print("3 -> Mostrar Jugadores")
        print("4 -> Mostrar Enemigos")
        print("5 -> Mostrar Clases")
        print("6 -> Mostrar Razas")
        print("7 -> Mostrar Objetos")
        print("8 -> Seleccionar Personaje")
        print("9 -> Crear Nuevo Personaje")
        print("0 -> Salir")

        opcion = input("Elige una opción: \n")

        if opcion == "1":
            submenu_combate(jugador_activo)
            pausar()
        elif opcion == "2":
            submenu_mercado(jugador_activo)
        elif opcion == "3":
            mostrar_jugadores()
            pausar()
        elif opcion == "4":
            mostrar_enemigos()
            pausar()
        elif opcion == "5":
            mostrar_clases()
            pausar()
        elif opcion == "6":
            mostrar_razas()
            pausar()
        elif opcion == "7":
            mostrar_objetos()
            pausar()
        elif opcion == "8":
            nuevo_personaje = seleccionar_personaje(jugadores, jugador_activo.nombre_usuario)
            if nuevo_personaje is not None:
                jugador_activo = nuevo_personaje
            else:
                print("No se seleccionó ningún personaje. Se mantiene el actual. \n")
                pausar()        
        elif opcion == "9":
            crear_nuevo_personaje(jugador_activo.nombre_usuario)
        elif opcion == "0":
            print("¡Gracias por jugar World of Pythoncraft! \n")
            pausar()
            iniciar_sesion()
        else:
            print("Opción inválida.")
            pausar()


#Ejecutacion Principal

if __name__ == "__main__":
    main()
    
