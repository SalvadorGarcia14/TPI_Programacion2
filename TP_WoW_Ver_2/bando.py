from typing import List
from raza import Raza


class Bando():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__razas:List[Raza] = []
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def razas(self) -> List[Raza]:
        return self.__razas
    @razas.setter
    def razas(self, nuevas_razas:List[Raza]):
        self.__razas = nuevas_razas

    def agregar_raza(self, nombre_raza):
        raza = Raza(nombre_raza, self)
        self.razas.append(raza)
        raza.bando = self  # relación inversa: la raza ahora sabe quién es su bando
        
    def obtener_razas(self):
        return self.razas
    
    def __str__(self):
        return f"Bando: {self.nombre} | Razas: [ {len(self.razas)} ]"