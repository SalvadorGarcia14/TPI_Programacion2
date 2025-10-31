from typing import List
from clase_personaje import ClasePersonaje  # si la necesitas

class Raza:
    def __init__(self, nombre: str, bando: str, clases_disponibles: List[ClasePersonaje]):
        self.__nombre = nombre
        self.__bando = bando
        self.__clases_disponibles = clases_disponibles

    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def bando(self):
        return self.__bando
    @bando.setter   
    def bando(self, bando):
        self.__bando = bando
    
    @property
    def clases_disponibles(self) -> List[ClasePersonaje]:
        return self.__clases_disponibles
    @clases_disponibles.setter  
    def clases_disponibles(self, nuevas_clases: List[ClasePersonaje]):
        self.__clases_disponibles = nuevas_clases
    
    def puede_usar_clase(self, nombre_clase: str) -> bool:
        return any(c.nombre == nombre_clase for c in self.clases_disponibles)
    
    def obtener_bando(self) -> str:
        return self.bando if self.bando else None
    
    def __str__(self):
        clases_nombres = ', '.join([c.nombre for c in self.clases_disponibles])
        return f"Raza: {self.nombre} | Bando: {self.bando} | Clases Disponibles: {clases_nombres}"
