class Enemigo:
    tipo_Enemigo: str
    puntos_energia: int = 10
    ataque = 1

    def __init__(self, tipo_Enemigo, puntos_energia=10, ataque=1):
        self._tipo_Enemigo = tipo_Enemigo
        self.puntos_energia = puntos_energia
        self.ataque = ataque

        def get_tipo_Enemigo(self):
            return self.__tipo_Enemigo

        def habla(self):
            print(f"Yo soy {self.__tipo_Enemigo}.preparando para pelear!!")

        def camina(self):
            print(f"{self.__tipo_Enemigo} se mueve cerca de ti!!! ")

        def atacar(self):
            print(f"{self.__tipo_Enemigo} ataca con un {self.ataque}de dar")     