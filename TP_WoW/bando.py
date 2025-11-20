from typing import List

class Bando():
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__razas: List = []


    @property
    def nombre(self):
        return self.__nombre

    @property
    def razas(self):
        return self.__razas

    def agregarRaza(self, raza):
        if raza not in self.razas:
            self.razas.append(raza)
    
    def __str__(self) -> str:
        nombres = []
        for raza in self.razas:
            nombres.append(raza.nombre)
        razas_nombres = ', '.join(nombres)        
        return f"Bando: {self.__nombre}, Razas: {razas_nombres}"