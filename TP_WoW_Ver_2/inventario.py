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
    
    # Getters Y Setters
    
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
    
    #Metodos
    
    def agregar_objeto(self, objeto: Objeto) -> str: #Agrega un objeto al inventario si hay espacio disponible
        if len(self.objetos) >= 20: #Limite 20 objetos
            print("El inventario está lleno.")
            return
        self.objetos.append(objeto)
        print(f"{objeto.nombre} agregado al inventario.")
    
        
    def remover_objeto(self, objeto: Objeto) -> str: #Elimina un objeto del inventario si existe
        if objeto in self.objetos:
            self.objetos.remove(objeto)
        else:
            return f"El objeto {objeto.nombre} no está en el inventario."
    
    def mostrar_objetos(self) -> List[Objeto]: #Devuelve la lista completa de objetos presentes
        return self.objetos
    
    def modificar_oro(self, cantidad: int): # Modifica la cantidad de oro sumando o restando el valor recibido
        self.oro += cantidad
        return self.__oro
    
    #Metodos de interacción con objetos
    
    def usar_objeto(self, jugador, indice): #Ejecuta la acción del objeto según su tipo
        #Consumible: aplica efectos y se elimina del inventario
        #Equipable: aplica efectos y se mueve a la lista de equipados
        objeto = self.objetos[indice] # Accede al objeto seleccionado mediante indice

        if objeto.tipo == "consumible": #Si el objeto es consumible, se usa una vez y se elimina
            jugador.aplicar_efecto(objeto.efectos) # Aplica los efectos del objeto
            print(f"Usaste {objeto.nombre}.")
            self.objetos.pop(indice)

        elif objeto.tipo == "equipable": # Si es equipable, se agregan efectos y se marca como equipado
            if objeto in self.equipados:
                print("Ese objeto ya está equipado.")
            else:
                jugador.aplicar_efecto(objeto.efectos) # Aplica efectos de equipamiento
                self.equipados.append(objeto)# Lo añade a la lista de equipados
                print(f"Equipaste {objeto.nombre}.")
        else:
            # Cualquier otro tipo de objeto no válido
            print("Este objeto no se puede consumir o equipar")
    
    
    def desequipar(self, jugador, indice): # Quita un objeto equipable:
        #Remueve sus efectos del jugador
        #Lo retira de la lista de equipados
        objeto = self.equipados[indice]#  Se obtiene el objeto equipado
        jugador.remover_efecto(objeto.efectos) # Se quitan los efectos aplicados
        self.equipados.remove(objeto)
        print(f"Desequipaste {objeto.nombre}.")
    
    
    def __str__(self):
        return f"Inventario ID: {self.id_inventario} | Oro: {self.oro} | Objetos: [ {len(self.objetos)} ]"

        

