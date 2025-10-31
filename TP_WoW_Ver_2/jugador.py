from personaje import Personaje
from typing import List


class Jugador(Personaje):
    
    _nombres_usuarios = set()  # Conjunto para rastrear nombres de usuario únicos
    
    def __init__(self, nombre: str, nivel: int, salud: int, mana: int, 
                 clase_personaje, inventario, nombre_usuario: str, experiencia: int, defensa: int ,nivel_maximo: int = 100):
        
        super().__init__(nombre, nivel, salud, mana, clase_personaje, inventario)
        
        if nombre_usuario in Jugador._nombres_usuarios:
            raise ValueError(f"El nombre de usuario '{nombre_usuario}' ya está en uso. Por favor, elija otro.")
        
        self.__nombre_usuario = nombre_usuario
        self.__experiencia = experiencia
        self.__defensa = defensa
        self.__nivel_maximo = nivel_maximo
        
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
    def nivel_maximo(self) -> int:
        return self.__nivel_maximo
    @nivel_maximo.setter
    def nivel_maximo(self, nuevo_nivel_maximo: int):
        self.__nivel_maximo = nuevo_nivel_maximo
    
    def atacar(self, objetivo, habilidad):
        if habilidad in self.clase_personaje.habilidades:
            if self.mana >= habilidad.costo_mana:
                self.mana -= habilidad.costo_mana
                daño_total = habilidad.daño + self.clase_personaje.poder_base
                objetivo.salud -= daño_total
                return (f"{self.nombre} usó {habilidad.nombre} contra {objetivo.nombre}, causando {daño_total} de daño."
                        f" Mana restante: {self.mana}.")
            else:
                return f"{self.nombre} no tiene suficiente mana para usar {habilidad.nombre}."
        else:
            return f"{self.nombre} no posee la habilidad {habilidad.nombre}."   

    def recibir_daño(self, cantidad):
        self.salud -= cantidad
        if self.salud <= 0:
            self.salud = 0
            return f"{self.nombre} ha sido derrotado."
        return f"{self.nombre} recibe {cantidad} de daño. Salud restante: {self.salud}."
    
    def subir_nivel(self):
        if self.nivel < self.nivel_maximo:
            self.nivel += 1
            
        #Aumenta salud y mana según la clase del personaje
        
        if self.clase_personaje.nombre == "guerrero":
            self.salud += 20
            self.mana += 5
        elif self.clase_personaje.nombre == "mago":
            self.salud += 10
            self.mana += 20
        elif self.clase_personaje.nombre == "cazador":
            self.salud += 15
            self.mana += 10
        elif self.clase_personaje.nombre == "druida":
            self.salud += 15
            self.mana += 15
        elif self.clase_personaje.nombre == "paladin":
            self.salud += 25
            self.mana += 10
        elif self.clase_personaje.nombre == "brujo":
            self.salud += 10
            self.mana += 25
        elif self.clase_personaje.nombre == "chaman":
            self.salud += 20
            self.mana += 15
            
            self.experencia = 0  # Reiniciar experiencia al subir de nivel
            return f"{self.nombre} ha subido al nivel {self.nivel}!"
        
        else:
            return f"{self.nombre} ya ha alcanzado el nivel máximo {self.nivel_maximo}."
    
    def calcular_experiencia_nivel(self):
        """Retorna la experiencia necesaria para pasar al siguiente nivel."""
        return 100 * (2 ** (self.nivel - 1))

    def ganar_experiencia(self, cantidad):
        """
        Gana experiencia y sube de nivel si alcanza la experiencia requerida.
        Cada nivel requiere el doble de experiencia que el anterior.
        """
        self.experiencia += cantidad
        mensaje = f"{self.nombre} ha ganado {cantidad} puntos de experiencia.\n"

        # Calcular experiencia necesaria para subir al siguiente nivel
        experiencia_necesaria = self.calcular_experiencia_nivel()

        # Mientras el jugador tenga suficiente experiencia para subir
        while self.experiencia >= experiencia_necesaria and self.nivel < self.nivel_maximo:
            self.experiencia -= experiencia_necesaria
            self.nivel += 1

            # Aumentar salud y maná según la clase del personaje
            clase = self.clase_personaje.nombre.lower()

            if clase == "guerrero":
                self.salud += 20
                self.mana += 5
            elif clase == "mago":
                self.salud += 10
                self.mana += 20
            elif clase == "cazador":
                self.salud += 15
                self.mana += 10
            elif clase == "druida":
                self.salud += 15
                self.mana += 15
            elif clase == "paladin":
                self.salud += 25
                self.mana += 10
            elif clase == "brujo":
                self.salud += 10
                self.mana += 25
            elif clase == "chaman":
                self.salud += 20
                self.mana += 15

            mensaje += f"🎉 {self.nombre} ha subido al nivel {self.nivel}! Salud: {self.salud}, Maná: {self.mana}\n"

            # Recalcular la nueva experiencia necesaria para el próximo nivel
            experiencia_necesaria = self.calcular_experiencia_nivel()

        if self.nivel >= self.nivel_maximo:
            mensaje += f"{self.nombre} ha alcanzado el nivel máximo ({self.nivel_maximo}).\n"

        return mensaje
    
    def __str__(self):
        return (f"Jugador: {self.nombre} | Usuario: {self.nombre_usuario} | Nivel: {self.nivel} | "
                f"Salud: {self.salud} | Mana: {self.mana} | Experiencia: {self.experiencia} | "
                f"Clase: {self.clase_personaje.nombre}")
