from typing import List
from objeto import Objeto

class Inventario():
    
    _contador_de_inventarios = 0  # Atributo de clase para llevar el conteo de instancias
    
    def __init__(self, oro: int, objetos: List[Objeto]):
        
        Inventario._contador_de_inventarios += 1
        self.__id_inventario = Inventario._contador_de_inventarios
        
        self.__oro = oro
        self.__objetos = objetos
        self.__equipados: List = [] 
    
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
    def objetos(self) -> List[Objeto]:
        return self.__objetos

    @property
    def equipados(self) -> List[Objeto]:
        return self.__equipados
    
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
    
    def mostrar_objetos(self) -> List[Objeto]:
        return self.objetos
    
    def modificar_oro(self, cantidad: int):
        self.oro += cantidad
        return self.__oro
    
    
    
    def usar_objeto(self, jugador, indice):
        objeto = self.objetos[indice]

        if objeto.tipo == "consumible":
            jugador.aplicar_efecto(objeto.efectos)
            print(f"Usaste {objeto.nombre}.")
            self.objetos.pop(indice)

        elif objeto.tipo == "equipable":
            if objeto in self.equipados:
                print("Ese objeto ya está equipado.")
            else:
                jugador.aplicar_efecto(objeto.efectos)
                self.equipados.append(objeto)
                print(f"Equipaste {objeto.nombre}.")
    
    
    def desequipar(self, jugador, indice):
        objeto = self.equipados[indice]
        jugador.remover_efecto(objeto.efectos)
        self.equipados.remove(objeto)
        print(f"Desequipaste {objeto.nombre}.")
    
    
    def __str__(self):
        return f"Inventario ID: {self.id_inventario} | Oro: {self.oro} | Objetos: [ {len(self.objetos)} ]"

        

