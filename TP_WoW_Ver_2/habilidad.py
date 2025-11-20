
class Habilidad():
    def __init__(self, nombre: str, tipo: str, costo_mana: int, daño: int):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__costo_mana = costo_mana
        self.__daño = daño

    # Getters Y Setters
   
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
    def costo_mana(self) -> int:
        return self.__costo_mana
    @costo_mana.setter
    def costo_mana(self, nuevo_costo_mana: int):
        self.__costo_mana = nuevo_costo_mana
    
    @property
    def daño(self) -> int:
        return self.__daño
    @daño.setter
    def daño(self, daño: int):
        self.__daño = daño
    

    def __str__(self):
        return f"Habilidad: {self.nombre} | Tipo: {self.tipo} | Costo de Mana: {self.costo_mana} | Daño: {self.daño}"
