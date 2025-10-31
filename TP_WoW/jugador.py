from personaje import Personaje

from typing import List

class Jugador(Personaje):
    def __init__(self, nombre, nivel, salud, mana, clase_personaje, inventario, nivel_maximo: int = 100):
        super().__init__(nombre, nivel, salud, mana, clase_personaje, inventario) 
        self.__nivel_maximo = nivel_maximo
        self.__experiencia = 0
    
    @property
    def nivel_maximo(self) -> int:
        return self.__nivel_maximo
    
    @property
    def experiencia(self) -> int:
        return self.__experiencia
    @experiencia.setter
    def experiencia(self, nueva_experiencia: int):
        self.__experiencia = nueva_experiencia
    
    
    def atacar(self, objetivo: Personaje) -> str:
        habilidades = self.habilidades + self.clase_personaje.habilidades_clase
        if not habilidades:
            return f"{self.nombre} no tiene habilidades para atacar."
        
        print(f"Habilidades disponibles para {self.clase_personaje.habilidades}:")
        for idx, habilidad in enumerate(habilidades, start=1):
            print(f"{idx}. {habilidad.nombre} (Daño: {habilidad.dano}, Costo de Mana: {habilidad.costo_mana})")
        eleccion = int(input("Seleccione el número de la habilidad que desea usar: ")) - 1
        
        if eleccion < 0 or eleccion >= len(habilidades):
            return "Selección inválida."
        habilidad_seleccionada = habilidades[eleccion]
        
        if self.mana < habilidad_seleccionada.costo_mana:
            return f"{self.nombre} no tiene suficiente mana para usar {habilidad_seleccionada.nombre}."
        self.mana -= habilidad_seleccionada.costo_mana
        objetivo.salud -= habilidad_seleccionada.dano
        
        return (f"{self.nombre} usa {habilidad.nombre} contra {objetivo.nombre}, "
                f"causando {habilidad.daño} de daño. "
                f"{objetivo.nombre} ahora tiene {objetivo.salud} de salud.")