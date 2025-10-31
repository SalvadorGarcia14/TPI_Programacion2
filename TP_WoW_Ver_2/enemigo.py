from personaje import Personaje
from typing import List

import random
import string

class Enemigo(Personaje):
    
    _nombres_enemigos = set()  # Conjunto para rastrear nombres de enemigos únicos
    
    def __init__(self, nombre: str, nivel: int, salud: int, mana: int, 
                 clase_personaje, inventario, tipo_enemigo: str, recompensa_experiencia: int):
        
        super().__init__(nombre, nivel, salud, mana, clase_personaje, inventario)
        
        if nombre in Enemigo._nombres_enemigos:
            raise ValueError(f"El nombre de enemigo '{nombre}' ya está en uso. Por favor, elija otro.")
        
        self.__tipo_enemigo = tipo_enemigo
        self.__recompensa_experiencia = recompensa_experiencia
    
    @property
    def tipo_enemigo(self) -> str:
        return self.__tipo_enemigo
    @tipo_enemigo.setter
    def tipo_enemigo(self, nuevo_tipo_enemigo: str):
        self.__tipo_enemigo = nuevo_tipo_enemigo
    
    @property
    def recompensa_experiencia(self) -> int:
        return self.__recompensa_experiencia
    @recompensa_experiencia.setter
    def recompensa_experiencia(self, nueva_recompensa_experiencia: int):
        self.__recompensa_experiencia = nueva_recompensa_experiencia
    
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
    
    def calcular_experiencia_nivel(self):
        """
        Los enemigos no suben de nivel como los jugadores,
        pero se implementa el método abstracto para cumplir con la clase base.
        """
        return 0

    def calcular_recompensa(self) -> int:
        nivel_factor = self.nivel * 10
        tipo_factor = {
            "común": 1,
            "raro": 2,
            "épico": 3,
            "legendario": 5
        }.get(self.tipo_enemigo.lower(), 1)
        
        recompensa = nivel_factor * tipo_factor
        return recompensa
    
    
    def __str__(self):
        return (f"Enemigo: {self.nombre} | Tipo: {self.tipo_enemigo} | Nivel: {self.nivel} | "
                f"Salud: {self.salud} | Mana: {self.mana} | Recompensa Experiencia: {self.recompensa_experiencia}")