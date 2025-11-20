from typing import List
from bando import Bando

class Raza():
    def __init__(self, nombre: str, bando: Bando, clases_disponibles: List[str]):
        self.__nombre = nombre
        self.__bando = bando
        self.__clases_disponibles = clases_disponibles
        bando.agregarRaza(self)
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def bando(self) -> Bando:
        return self.__bando
    
    @property
    def clases_disponibles(self) -> List[str]:
        return self.__clases_disponibles
    
    def puede_usar_clase(self, clase: str) -> bool:
        return clase in self.__clases_disponibles
    
    def __str__(self) -> str:
        return f"Raza: {self.__nombre}, Bando: {self.__bando.nombre}, Clases Disponibles: {', '.join(self.__clases_disponibles)}"
