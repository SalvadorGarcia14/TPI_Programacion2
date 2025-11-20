from typing import List
from bando import Bando
from clase_personaje import ClasePersonaje  

class Raza():
    def __init__(self, nombre: str, bando: Bando, clases_disponibles: List[ClasePersonaje]):
        self.__nombre = nombre
        self.__bando = bando
        self.__clases_disponibles = clases_disponibles
        self.__razas:List = []

    # Getters Y Setters
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def bando(self) -> Bando:
        return self.__bando
    @bando.setter
    def bando(self, nuevo_bando: str) -> Bando:
        self.__bando = nuevo_bando
    
    @property
    def razas(self) -> Bando:
        return self.__razas
    
    @property
    def clases_disponibles(self) -> List[ClasePersonaje]:
        return self.__clases_disponibles
    @clases_disponibles.setter  
    def clases_disponibles(self, nuevas_clases: List[ClasePersonaje]):
        self.__clases_disponibles = nuevas_clases
    
    #Metodos
    
    def puede_usar_clase(self, nombre_clase: str) -> bool: #Verifica si esta raza puede usar una clase específica
        for clase in self.clases_disponibles:
            if clase.nombre == nombre_clase:
                return True
        return False
    
    def agregar_bando_a_la_raza(self, nuevo_bando: Bando) -> None: #Verifica la entrada y el bando de la raza
        if not isinstance(nuevo_bando, Bando):
            print("El bado debe ser una instancia de la clase Bando")
            return
        self.__bando = nuevo_bando
        
    
    def __str__(self):
        clases_nombres = []
        for clase in self.clases_disponibles:
            clases_nombres.append(clase.nombre)
        clase_disponibles = ",".join(clases_nombres) #Une las clases en una sola línea separada por comas

        return f"Raza: {self.nombre} | Bando: {self.bando} | Clases Disponibles: {clase_disponibles}"
