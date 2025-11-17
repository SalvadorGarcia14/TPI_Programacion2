
from habilidad import Habilidad
from typing import List

class ClasePersonaje():
    
    _contador_clases_personaje = 0  # Contador Id
    
    def __init__(self, nombre: str, rol: str, poder_base: int, habilidades: List[Habilidad]):
        
        self.__id_clase_personaje = ClasePersonaje._contador_clases_personaje
        ClasePersonaje._contador_clases_personaje += 1  # Incrementar el contador
        
        if not isinstance(poder_base, int) or poder_base < 0:
            raise ValueError("El poder base debe ser un entero no negativo.")
        
        if not isinstance(habilidades, list) or len(habilidades) < 3:
            raise ValueError("Debe proporcionar al menos tres habilidades.")
        
        self.__nombre = nombre
        self.__rol = rol #Tank, Healer, DPS
        self.__poder_base = poder_base
        self.__habilidades = habilidades
        
        
    @property
    def id_clase_personaje(self) -> int:
        return self.__id_clase_personaje
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre
    
    @property
    def rol(self) -> str:
        return self.__rol
    @rol.setter
    def rol(self, rol: str):
        self.__rol = rol
    
    @property
    def poder_base(self) -> int:
        return self.__poder_base
    @poder_base.setter  
    def poder_base(self, poder_base: int):
        self.__poder_base = poder_base
    
    @property
    def habilidades(self) -> List[Habilidad]:
        return self.__habilidades
    
    def agregar_habilidad(self, habilidad: Habilidad) -> None:
        if habilidad not in self.habilidades:
            self.habilidades.append(habilidad)
        else:
            return f"La habilidad {habilidad.nombre} ya está en la lista de habilidades."
    
    def obtener_habilidades(self) -> List[Habilidad]:
        return self.habilidades
    
    def __str__(self):
        habilidades_nombres = []
        for habilidad in self.habilidades:
            habilidades_nombres.append(habilidad.nombre)
        habilidades_str = ", ".join(habilidades_nombres)
        
        return (
            f"ClasePersonaje ID: {self.id_clase_personaje} | Nombre: {self.nombre} | Rol: {self.rol} | "
            f"Poder Base: {self.poder_base} | Habilidades: [ {habilidades_str} ]"
        )
            