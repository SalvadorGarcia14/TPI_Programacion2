from abc import ABC, abstractmethod
from clase_de_personaje import ClaseDePersonaje
from inventario import Inventario

from typing import List #Si nbo se usa borrar

class Personaje(ABC):
    
    _contador_personajes = 0
    
    def __init__(self, nombre: str, nivel: int, salud: int, mana: int, 
                clase_personaje: ClaseDePersonaje, inventario: Inventario):
    
        self.id_personaje = Personaje._contador_personajes
        Personaje._contador_personajes += 1
        
        self.__nombre = nombre
        self.__nivel = nivel
        self.__salud = salud
        self.__mana = mana
        self.__clase_personaje = clase_personaje
        self.__habilidades:list = []
        self.__inventario = inventario
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    @property
    def nivel(self) -> int:
        return self.__nivel
    
    @property
    def salud(self) -> int:
        return self.__salud
    @salud.setter
    def salud(self, nueva_salud: int):
        self.__salud = nueva_salud
    
    @property
    def mana(self) -> int:
        return self.__mana
    @mana.setter
    def mana(self, nuevo_mana: int):
        self.__mana = nuevo_mana
    
    @property
    def clase_personaje(self) -> ClaseDePersonaje:
        return self.__clase_personaje
    
    @property
    def habilidades(self) -> List:
        return self.__habilidades

    @property
    def inventario(self) -> Inventario:
        return self.__inventario    
    
    
    # ===========================
    # Métodos de instancia
    # ===========================
    
    @abstractmethod
    def atacar(self, objetivo, habilidad):
        """Método abstracto: será implementado en Jugador y Enemigo."""
        pass
    
    def subir_nivel(self) -> str:
        if self.nivel < 100:
            self.nivel += 1
            
            clase = self.clase_personaje.nombre.lower()
            if clase == "guerrero":
                self.salud += 10
                self.mana += 3
            elif clase == "mago":
                self.salud += 5
                self.mana += 10
            elif clase == "cazador":
                self.salud += 7
                self.mana += 7
            elif clase == "paladín":
                self.salud += 8
                self.mana += 6
            elif clase == "druida":
                self.salud += 6
                self.mana += 8
            elif clase == "chaman":
                self.salud += 7
                self.mana += 7
            elif clase == "brujo":
                self.salud += 6
                self.mana += 10
            else:
                return "Clase desconocida. No se han aplicado mejoras de salud y mana."
            self._experiencia = 0
        else:
            print("El personaje ya ha alcanzado el nivel máximo.")
        
        return (f"{self.nombre} ha subido al nivel {self.nivel}! "
                f"Salud: {self.salud}, Maná: {self.mana}.")
    
    def asignar_inventario(self, inventario_personaje: Inventario) -> str:
        if isinstance(inventario_personaje, Inventario):
            self.inventario = inventario_personaje
            return f"Inventario asignado al personaje {self.nombre}."
        else:
            return "Error: El inventario proporcionado no es válido."
    
    def mostrar_habilidades(self) -> None:

        habilidades_clase = self.clase_personaje.habilidades
        
        habilidades_personaje = self.habilidades
        
        habilidades_totales = list(habilidades_clase)  # Copiar habilidades de la clase
        for hab in habilidades_personaje:
            if hab not in habilidades_totales:
                habilidades_totales.append(hab)

        if not habilidades_totales:
            print(f"El personaje {self.nombre} no tiene habilidades asignadas.")
        
        #Mostrar habilidades
        salida = f"Habilidades del personaje {self.nombre} [{self.clase_personaje.nombre}]: \n"
        for habilidad in habilidades_totales:
            salida += f"- {habilidad}\n"
        
        return salida

    # ===========================
    # Métodos de clase
    # ===========================
    
    @classmethod
    def cantidadPersonajes(cls) -> int:
        return cls._contador_personajes
    
    def __str__(self) -> str:
        habs = self.mostrar_habilidades()
        
        objetos = []
        for objeto in self.inventario.objetos:
            objetos.append(objeto.nombre)
        objetos_nombres = ', '.join(objetos)
        
        return (f"Personaje(ID: {self.id_personaje}, Nombre: {self.nombre}, Nivel: {self.nivel}, Salud: {self.salud}, Mana: {self.mana}, \n"
                f"Clase: {self.clase_personaje.nombre}, \n"
                f"{habs}"
                f"Inventario(ID) : {self.inventario.id_inventario}, Oro: {self.inventario.oro}, "
                f"Objetos: ({objetos_nombres})\n")

