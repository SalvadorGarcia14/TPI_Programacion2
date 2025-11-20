from personaje import Personaje
from typing import List


class Jugador(Personaje):
    
    _nombres_usuarios = set()  # Conjunto para rastrear nombres de usuario únicos
    
    def __init__(self, nombre: str, nivel: int, salud: int,salud_maxima ,mana: int,mana_maxima: int,  
                 clase_personaje, inventario, nombre_usuario: str, experiencia: int, defensa: int, ataque: int, nivel_maximo: int = 100):
        
        super().__init__(nombre, nivel, salud,salud_maxima ,mana,mana_maxima, clase_personaje, inventario)
        
        if nombre_usuario in Jugador._nombres_usuarios:
            raise ValueError(f"El nombre de usuario '{nombre_usuario}' ya está en uso. Por favor, elija otro.")
        
        self.__nombre_usuario = nombre_usuario
        self.__experiencia = experiencia
        self.__defensa = defensa
        self.__ataque = ataque
        self.__nivel_maximo = nivel_maximo
    
    # Getters Y Setters
    
    @property
    def nombre_usuario(self) -> str:
        return self.__nombre_usuario
    @nombre_usuario.setter
    def nombre_usuario(self, nuevo_nombre_usuario: str):
        self.__nombre_usuario = nuevo_nombre_usuario
    
    @property
    def experiencia(self) -> int:
        return self.__experiencia
    @experiencia.setter
    def experiencia(self, nueva_experiencia: int):
        self.__experiencia = nueva_experiencia
    
    @property
    def defensa(self) -> int:
        return self.__defensa
    @defensa.setter
    def defensa(self, nueva_defensa: int):
        self.__defensa = nueva_defensa

    @property
    def ataque(self) -> int:
        return self.__ataque
    @ataque.setter
    def ataque(self, nueva_ataque: int):
        self.__ataque = nueva_ataque
    
    @property
    def nivel_maximo(self) -> int:
        return self.__nivel_maximo
    @nivel_maximo.setter
    def nivel_maximo(self, nuevo_nivel_maximo: int):
        self.__nivel_maximo = nuevo_nivel_maximo
    
    #Metodos
    
    def resetear_mana(self) -> int:
        self.mana = self.mana_maxima
    
    def atacar(self, objetivo, habilidad): #Logica de ataque
        if habilidad in self.clase_personaje.habilidades: #Validamos las habilidades pertenezcan a la clase del jugador
            if self.mana >= habilidad.costo_mana: #Validamos mana sufiente
                self.mana -= habilidad.costo_mana #Restamos mana usado
                daño_total = habilidad.daño + self.clase_personaje.poder_base + self.ataque #Calculo del daño total / daño habilidad + poder base de la clase + ataque del jugador
                objetivo.salud -= daño_total #Restamos daño a la salud del objetivo
                return (f"{self.nombre} usó {habilidad.nombre} contra {objetivo.nombre}, causando {daño_total} de daño."
                        f" Mana restante: {self.mana}.")
            else:
                return f"{self.nombre} no tiene suficiente mana para usar {habilidad.nombre}."
        else:
            return f"{self.nombre} no posee la habilidad {habilidad.nombre}."   

    def recibir_daño(self, cantidad): #Logica de Recibir daño
        self.salud -= cantidad #Descuenta el daño recibido
        if self.salud < 0: #Si la salud baja de cero, queda en 0 y se considera derrotado
            self.salud = 0
            return f"{self.nombre} ha sido derrotado."
        return f"{self.nombre} recibe {cantidad} de daño. Salud restante: {self.salud}."
    
    
    def calcular_experiencia_nivel(self): #Cálculo de experiencia necesaria por nivel (nivel_n = 100 * 2^(nivel-1))
        """Retorna la experiencia necesaria para pasar al siguiente nivel."""
        return 100 * (2 ** (self.nivel - 1))

    def ganar_experiencia(self, cantidad):
        """
        Gana experiencia y sube de nivel si alcanza la experiencia requerida.
        Cada nivel requiere el doble de experiencia que el anterior.
        """
        self.experiencia += cantidad # Se suma la experiencia ganada
        mensaje = f"{self.nombre} ha ganado {cantidad} puntos de experiencia.\n"

        while self.nivel < self.nivel_maximo: # Bucle para subir múltiples niveles si existe suficiente experiencia 
            experiencia_necesaria = self.calcular_experiencia_nivel()

            #Si alcanza la experiencia necesaria, sube de nivel
            if self.experiencia >= experiencia_necesaria: 
                self.experiencia -= experiencia_necesaria #Se descuenta la experencia
                self.nivel += 1 #Y sube de nivel

                clase = self.clase_personaje.nombre.lower() #Bonus por clase

                if clase == "guerrero":
                    self.salud += 20
                    self.mana += 5
                    self.ataque += 10
                elif clase == "mago":
                    self.salud += 10
                    self.mana += 20
                    self.ataque += 5
                elif clase == "cazador":
                    self.salud += 15
                    self.mana += 10
                    self.ataque += 15
                elif clase == "druida":
                    self.salud += 15
                    self.mana += 15
                    self.ataque += 10
                elif clase == "paladin":
                    self.salud += 25
                    self.mana += 10
                    self.ataque += 12
                elif clase == "brujo":
                    self.salud += 10
                    self.mana += 25
                    self.ataque += 4
                elif clase == "chaman":
                    self.salud += 20
                    self.mana += 15
                    self.ataque += 10

                mensaje += f"🎉 {self.nombre} ha subido al nivel {self.nivel}! Salud: {self.salud}, Daño Basico: {self.ataque} ,Maná: {self.mana}\n"

            else:
                break  # No alcanza experiencia para el siguiente nivel

        # Si llegó al máximo nivel, bloquear progreso y reiniciar experiencia
        if self.nivel >= self.nivel_maximo:
            self.experiencia = 0
            mensaje += f"{self.nombre} ya ha alcanzado el nivel máximo {self.nivel_maximo}.\n"

        return mensaje

    def esta_vivo(self) -> bool: # Verifica si el jugador sigue vivo
        return self.salud > 0

    def agregar_objeto_inventario(self, objeto): #Delegamos en el inventario la acción de agregar objetos
        return self.inventario.agregar_objeto(objeto)

    def mostrar_inventario(self) -> List[str]:
        return self.inventario.mostrar_objetos()
    
    def ganar_oro(self, cantidad): # Gana oro usando la función del inventario
        self.inventario.modificar_oro(cantidad)
        return cantidad
    
    #Aplicar efectos de objetos o Buffs
    
    def aplicar_efecto(self, efectos: dict):
    
        if "vida" in efectos:
            self.salud = self.salud + efectos["vida"]
            if self.salud > self.salud_maxima: # Si se excede la vida máxima, se ajusta
                self.salud = self.salud_maxima

        if "vida_max" in efectos: 
            self.salud_maxima = self.salud_maxima + efectos["vida_max"]
            self.salud = self.salud + efectos["vida_max"] # Se otorga el aumento de vida adicional

        if "ataque" in efectos:
            self.ataque += efectos["ataque"]

        if "defensa" in efectos:
            self.defensa += efectos["defensa"]
    
    #Remuve los efectos temporales o Debuffs
    
    def remover_efecto(self, efectos: dict):
        if "vida_max" in efectos:
            if self.hp_actual > self.salud_maxima:
                self.hp_actual = self.salud_maxima         
    
        if "ataque" in efectos:
            self.ataque -= efectos["ataque"]

        if "defensa" in efectos:
            self.defensa_base -= efectos["defensa"]   
    
    
    
    def __str__(self):
        return (f"Jugador: {self.nombre} | Usuario: {self.nombre_usuario} | Nivel: {self.nivel} | "
                f"Salud: {self.salud} | Daño Basico: {self.ataque} | Mana: {self.mana} | Experiencia: {self.experiencia} | Oro: {self.inventario.oro} | "
                f"Clase: {self.clase_personaje.nombre}")
