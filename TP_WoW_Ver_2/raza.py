from typing import List
from clase_personaje import ClasePersonaje  

class Raza():
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
    def bando(self) -> str:
        return self.__bando
    @bando.setter   
    def bando(self, nuevo_bando) -> str:
        self.__bando = nuevo_bando
    
    @property
    def clases_disponibles(self) -> List[ClasePersonaje]:
        return self.__clases_disponibles
    @clases_disponibles.setter  
    def clases_disponibles(self, nuevas_clases: List[ClasePersonaje]):
        self.__clases_disponibles = nuevas_clases
    
    def puede_usar_clase(self, nombre_clase: str) -> bool:
        for clase in self.clases_disponibles:
            if clase.nombre == nombre_clase:
                return True
        return False
    
    def obtener_bando(self) -> str:
        if self.bando:
            return self.bando
        else:
            return None
    
    def __str__(self):
        clases_nombres = []
        for clase in self.clases_disponibles:
            clases_nombres.append(clase.nombre)
        clase_disponibles = ",".join(clases_nombres)

        return f"Raza: {self.nombre} | Bando: {self.bando} | Clases Disponibles: {clase_disponibles}"
