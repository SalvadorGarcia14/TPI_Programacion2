from typing import List
from objeto import Objeto

class Inventario():
    
    _contador_de_inventarios = 0  # Atributo de clase para llevar el conteo de instancias
    
    def __init__(self, oro: int, objetos: List[str]):
        
        self.__id_inventario = Inventario._contador_de_inventarios = 0  # Atributo de clase para llevar el conteo de instancias
        Inventario._contador_de_inventarios += 1 
        
        self.__oro = oro
        self.__objetos = objetos
    
    @property
    def id_inventario(self) -> int:
        return self.__id_inventario

    @property
    def oro(self) -> int:
        return self.__oro
    @oro.setter
    def oro(self, nuevo_oro: int):
        self.__oro = nuevo_oro
    
    @property
    def objetos(self) -> List[str]:
        return self.__objetos
    
    def agregar_objeto(self, objeto: Objeto) -> str:
        if len(self.objetos) >= 20:
            print("El inventario está lleno.")
            return
        self.objetos.append(objeto)
        print(f"{objeto.nombre} agregado al inventario.")
    
        
    def remover_objeto(self, objeto: Objeto) -> str:
        if objeto in self.objetos:
            self.objetos.remove(objeto)
        else:
            return f"El objeto {objeto.nombre} no está en el inventario."
    
    def mostrar_objetos(self) -> List[str]:
        return self.objetos
    
    def __str__(self):
        return f"Inventario ID: {self.id_inventario} | Oro: {self.oro} | Objetos: [ {len(self.objetos)} ]"

        

