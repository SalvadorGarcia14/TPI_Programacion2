from typing import List
from objeto import Objeto

class Inventario():
    def __init__(self, id_inventario: int, oro: int, objetos: List [Objeto]):
        self.id_inventario = id_inventario
        self.oro = oro
        self.objetos = objetos


        
