from personaje import Personaje
from typing import List

import random
import string

class Enemigo(Personaje):
    
    _nombres_enemigos = set()  
    
    def __init__(self, nombre: str, nivel: int, salud: int,salud_maxima: int, mana: int,mana_maxima:int,  
                 clase_personaje, inventario, tipo_enemigo: str, recompensa_experiencia: int, rango_oro: List[int]):
        
        super().__init__(nombre, nivel, salud,salud_maxima ,mana,mana_maxima, clase_personaje, inventario)
        
        if nombre in Enemigo._nombres_enemigos:
            raise ValueError(f"El nombre de enemigo '{nombre}' ya está en uso. Por favor, elija otro.")
        Enemigo._nombres_enemigos.add(nombre)
        
        self.__tipo_enemigo = tipo_enemigo
        self.__recompensa_experiencia = recompensa_experiencia
        self.__rango_oro = rango_oro
    
    # Getters Y Setters
    
    @property
    def tipo_enemigo(self) -> str:
        return self.__tipo_enemigo
    @tipo_enemigo.setter
    def tipo_enemigo(self, nuevo_tipo_enemigo) -> str:
        self.__tipo_enemigo = nuevo_tipo_enemigo
    
    @property
    def recompensa_experiencia(self) -> int:
        return self.__recompensa_experiencia
    @recompensa_experiencia.setter
    def recompensa_experiencia(self, nuevo_recompensa_experiencia) -> int:
        self.recompensa_experiencia = nuevo_recompensa_experiencia

    @property
    def rango_oro(self) -> List:
        return self.__rango_oro

    #Metodos
    
    def atacar(self, objetivo, habilidad):
        if habilidad in self.clase_personaje.habilidades:#Validamos las habilidades pertenezcan a la clase del jugador
            if self.mana >= habilidad.costo_mana: #Validamos mana sufiente
                self.mana -= habilidad.costo_mana #Restamos mana usado
                daño_total = habilidad.daño + self.clase_personaje.poder_base #Calculo del daño total / daño habilidad + poder base de la clase
                resultado = objetivo.recibir_daño(daño_total) #Restamos daño a la salud del objetivo
                return f"{self.nombre} usó {habilidad.nombre} contra {objetivo.nombre}, causando {daño_total} de daño.\n{resultado} Mana restante: {self.mana}."
            else:
                return f"{self.nombre} no tiene suficiente mana para usar {habilidad.nombre}."
        else:
            return f"{self.nombre} no posee la habilidad {habilidad.nombre}."
    
    def recibir_daño(self, cantidad): #Logica de Recibir daño
        self.salud = max(0, self.salud - cantidad) #Nueva salud = salud actual - cantidad, pero nunca baja de 0
        if self.salud == 0: # Si llegó a 0, el enemigo muere
            return f"{self.nombre} ha sido derrotado."
        return f"{self.nombre} recibe {cantidad} de daño. Salud restante: {self.salud}."
    
    def resetear_salud(self): #Reset estadisticas
        """Restablece la salud del enemigo a la máxima."""
        self.salud = self.salud_maxima
    
    def resetear_mana(self): #Reset estadisticas
        """Restablece el mana del enemigo a la máxima."""
        self.mana = self.mana_maxima
    
    def calcular_experiencia_nivel(self): # Los enemigos no usan este sistema de niveles
        return 0

    def esta_vivo(self) -> bool:
        return self.salud > 0

    def agregar_objeto_inventario(self, objeto) -> None: # Los enemigos no agregan objetos a su inventario
        pass

    def mostrar_inventario(self) -> None:
        return []

    def calcular_recompensa(self) -> tuple[int, int]: #Calculo de experencia y oro
        #Formula segun el nivel y la rareza / EXP final = nivel_factor * tipo_factor
        # EXP
        nivel_factor = self.nivel * 10 
        tipo_factor = { # Multiplicador según tipo de enemigo
        "común": 1,
        "raro": 2,
        "épico": 3,
        "legendario": 5
        }.get(self.tipo_enemigo.lower(), 1)  # Valor por defecto: 1
    
        exp = nivel_factor * tipo_factor

        # Calculo de oro, entre maximos y minimos(rango_oro[0] -> minimo : rango_oro[1] -> maximo) definidos segun el tipo de enemigo  /EJ: rango [5, 12] -> devuelve entre 5 y 12
        oro = random.randint(self.rango_oro[0], self.rango_oro[1])

        return exp, oro
    
    def __str__(self):
        return (f"Enemigo: {self.nombre} | Tipo: {self.tipo_enemigo} | Nivel: {self.nivel} | "
                f"Salud: {self.salud}/{self.salud_maxima} | Mana: {self.mana} | Recompensa Experiencia: {self.recompensa_experiencia}")