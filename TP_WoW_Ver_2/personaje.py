from abc import ABC, abstractmethod
from typing import List

from clase_personaje import ClasePersonaje
from inventario import Inventario
from habilidad import Habilidad


class Personaje(ABC):

    _contador_id_personajes = 0  # Atributo de clase para llevar el conteo de instancias
    
    def __init__(self, nombre: str, nivel: int, salud: int,salud_maxima: int ,mana: int, mana_maxima: int,
                clase_personaje: ClasePersonaje, inventario: Inventario):
        
        self.__id_personaje = Personaje._contador_id_personajes
        Personaje._contador_id_personajes += 1  # Incrementar el contador
        
        if isinstance(nivel, int) and nivel < 1:
            raise ValueError("El nivel debe ser un entero mayor o igual a 1.")
        
        self.__nombre = nombre
        self.__nivel = nivel
        self.__salud = salud
        self.__salud_maxima = salud_maxima 
        self.__mana = mana
        self.__mana_maxima = mana_maxima
        
        self.__clase_personaje = clase_personaje
        self.__inventario = inventario
        
        self.__habilidades: List[Habilidad] = clase_personaje.obtener_habilidades()
    
    @property
    def id_personaje(self) -> int:
        return self.__id_personaje
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    @property
    def nivel(self) -> int:
        return self.__nivel
    @nivel.setter
    def nivel(self, nuevo_nivel: int):
        self.__nivel = nuevo_nivel
    
    @property
    def salud(self) -> int:
        return self.__salud
    @salud.setter
    def salud(self, nueva_salud: int):
        self.__salud = max(0, nueva_salud) 

    @property
    def salud_maxima(self) -> int:
        return self.__salud_maxima

    @salud_maxima.setter
    def salud_maxima(self, nueva_salud_maxima: int):
        self.__salud_maxima = nueva_salud_maxima
    
    @property
    def mana(self) -> int:
        return self.__mana
    @mana.setter
    def mana(self, nuevo_mana: int):
        self.__mana = nuevo_mana
        
    @property
    def mana_maxima(self) -> int:
        return self.__mana_maxima
    @mana_maxima.setter
    def mana_maxima(self, nuevo_mana_maximo) -> int:
        self.__mana_maxima = nuevo_mana_maximo
        
    @property
    def clase_personaje(self) -> ClasePersonaje:
        return self.__clase_personaje
    
    @property
    def inventario(self) -> Inventario:
        return self.__inventario
    
    @property
    def habilidades(self) -> List[Habilidad]:
        return self.__habilidades
    
    @abstractmethod
    def atacar(self, objetivo, habilidad: Habilidad):
        """
        Método abstracto: será implementado por Jugador y Enemigo.
        Define cómo el personaje usa una habilidad para atacar a otro.
        """
        pass
    
    @abstractmethod
    def recibir_daño(self, cantidad: int) -> None:
        
        """
        Reduce la salud del personaje en la cantidad de daño recibida. Si la salud llega a 0 o menos, el personaje es derrotado.
        """
        pass
    
    @abstractmethod
    def calcular_experiencia_nivel(self):
        """Calcula la experiencia necesaria para subir de nivel"""
        pass
    
    def esta_vivo(self) -> bool:
        return self.salud > 0 #Indica si el personaje sigue con vida.
    
    def agregar_objeto_inventario(self, objeto):
        return self.inventario.agregar_objeto(objeto)
    
    def mostrar_inventario(self) -> List[str]:
        return self.inventario.mostrar_objetos()        
    
    def __str__(self):
        habilidades_nombres = []
        for habilidad in self.habilidades:
            habilidades_nombres.append(habilidad.nombre)
        habilidades_str = ", ".join(habilidades_nombres)
        
        return (
            f"Personaje ID: {self.id_personaje} | Nombre: {self.nombre} | Nivel: {self.nivel} | "
            f"Salud: {self.salud} | Mana: {self.mana} | Clase: {self.clase_personaje.nombre} | "
            f"Habilidades: [ {habilidades_str} ]"
        )
        