
from habilidad import Habilidad
from typing import List

class ClasePersonaje():
    
    _contador_clases_personaje = 0  # Contador globall Id
    
    def __init__(self, nombre: str, rol: str, poder_base: int, habilidades: List[Habilidad]):
        
        self.__id_clase_personaje = ClasePersonaje._contador_clases_personaje #asigna un ID unico
        ClasePersonaje._contador_clases_personaje += 1  # Incrementar el contador
        
        if not isinstance(poder_base, int) or poder_base < 0:
            raise ValueError("El poder base debe ser un entero no negativo.")
        
        if not isinstance(habilidades, list):
            raise ValueError("Debe proporcionar al menos tres habilidades.")
        
        self.__nombre = nombre
        self.__rol = rol #Tank, Healer, DPS
        self.__poder_base = poder_base
        self.__habilidades = habilidades
        
    # Getters Y Setters
 
    @property
    def id_clase_personaje(self) -> int:
        return self.__id_clase_personaje
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    @property
    def rol(self) -> str:
        return self.__rol
    @rol.setter
    def rol(self, nuevo_rol: str):
        self.__rol = nuevo_rol
    
    @property
    def poder_base(self) -> int:
        return self.__poder_base
    @poder_base.setter  
    def poder_base(self, nuevo_poder_base: int):
        self.__poder_base = nuevo_poder_base
    
    @property
    def habilidades(self) -> List[Habilidad]:
        return self.__habilidades
    
    #Metodos
    
    def agregar_habilidad(self, habilidad: Habilidad) -> None: #Agrega una habilidad y veririca que no este repetida
        if habilidad not in self.habilidades:
            self.habilidades.append(habilidad)
        else:
            return f"La habilidad {habilidad.nombre} ya está en la lista de habilidades."
    
    def obtener_habilidades(self) -> List[Habilidad]: #DevuelvE lista con los nombres de las habilidades
        habilidades_nombres = []
        for habilidad in self.habilidades:
            habilidades_nombres.append(habilidad.nombre)
        return habilidades_nombres
    
    def __str__(self):
        habilidades_str = ", ".join(self.obtener_habilidades()) #Une las clases en una sola línea separada por comas
        return (
            f"ClasePersonaje ID: {self.id_clase_personaje} | Nombre: {self.nombre} | Rol: {self.rol} | "
            f"Poder Base: {self.poder_base} | Habilidades: [ {habilidades_str} ]"
        )