from typing import List
from habilidad import Habilidad
from raza import Raza

from habilidad import Habilidad

class ClaseDePersonaje:
    
    _contador_clases = 0
    
    def __init__(self, nombre: str, rol: str, poder_base: int, raza: Raza, habilidades: List[Habilidad] = None):
        
        self.__id_clase = ClaseDePersonaje._contador_clases
        ClaseDePersonaje._contador_clases += 1
        
        if not isinstance(poder_base, int) or poder_base <= 0:
            raise ValueError("El poder base debe ser un entero positivo.")            
        
        self.__nombre = nombre
        self.__rol = rol #Tank, Healer, DPS
        self.__poder_base = poder_base
        self.__raza = raza
        self.__habilidades = habilidades if habilidades is not None else []
    

    @property
    def id_clase(self) -> int:
        return self.__id_clase
    
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
    
    @property
    def raza(self) -> Raza:
        return self.__raza
    
    @property
    def habilidades(self) -> List[Habilidad]:
        return self.__habilidades
    
    @classmethod
    def cantidadClases(cls) -> int:
        return cls._contador_clases
    
    def agregar_habilidad(self, habilidad: Habilidad):
        if habilidad not in self.habilidades:
            self.habilidades.append(habilidad)
        else:
            print(f"La habilidad {habilidad.nombre} ya está asignada a la clase {self.nombre}.")

    def __str__(self) -> str:
        #habilidades_nombres = ', '.join([habilidad.nombre for habilidad in self.habilidades])
        nombres = []
        for habilidad in self.habilidades:
            nombres.append(habilidad.nombre)
        habilidades_nombres = ', '.join(nombres)
        return (
            f"ClaseDePersonaje(ID: {self.id_clase}, Nombre: {self.nombre}, Rol: {self.rol}, Raza: {self.raza.nombre} \n"
            f"Poder Base: {self.poder_base},\n"
            f"Habilidades: {habilidades_nombres})\n"
        )

