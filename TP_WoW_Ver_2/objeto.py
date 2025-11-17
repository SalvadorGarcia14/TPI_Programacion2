from typing import Dict
import random
import string

class Objeto():
    def __init__(self, nombre: str, descripcion: str, tipo: str, efectos: Dict ,valor: int):
        
        self.__id_objeto = Objeto.generador_aleatorios_id_obejtos()
        
        self.__nombre = nombre
        self.__tipo = tipo
        self.__efectos = efectos
        self.__descripcion = descripcion
        self.__valor = valor
    
    
    @property
    def id_objeto(self) -> int:
        return self.__id_objeto

    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    @property
    def tipo(self) -> str:
        return self.__tipo
    @tipo.setter
    def tipo(self, nuevo_tipo: str):
        self.__tipo = nuevo_tipo

    @property
    def efectos(self) -> Dict:
        return self.__efectos
    
    @property
    def descripcion(self) -> str:
        return self.__descripcion   
    @descripcion.setter
    def descripcion(self, nueva_descripcion: str):
        self.__descripcion = nueva_descripcion
    
    @property
    def valor(self) -> int:
        return self.__valor
    @valor.setter
    def valor(self, nuevo_valor: int):
        self.__valor = nuevo_valor
        
    @classmethod
    def generador_aleatorios_id_obejtos(cls) -> str: #Genera un ID aleatorio de 3 a 6 caracteres numéricos.
        longitud_ids = random.randint(3, 6) # elige longitud aleatoria entre 3 y 6
        id_aleatorio = "".join(random.choices(string.digits, k=longitud_ids))
        return id_aleatorio
    
    def usar(self) -> str:
        return f"Usando el objeto: {self.nombre}"
    
    def __str__(self):
        return f"Objeto ID: {self.id_objeto} | Nombre: {self.nombre} | Descripción: {self.descripcion} | Valor: {self.valor} oro"