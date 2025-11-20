class Habilidad():
    def __init__(self, nombre: str, tipo: str, costo_mana: int, daño:int):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__costo_mana = costo_mana
        self.__daño = daño
    
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
    def costo_mana(self, nuevo_costo: int):
        self.__costo_mana = nuevo_costo
    
    @property
    def daño(self) -> int:
        return self.__daño
    @daño.setter
    def daño(self, nuevo_daño: int):
        self.__daño = nuevo_daño
        
    def __str__(self) -> str:
        return f"Habilidad: {self.__nombre}, Tipo: {self.__tipo}, Costo de Mana: {self.__costo_mana}, Daño: {self.__daño}"