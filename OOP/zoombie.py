from zoombie import *

class zoombie(Enemigo):
    def __init__(self, puntos_Energia=10,ataque=1):
        super().__init__(tipo_Enemigo='zoombie', puntos_Energia=puntos_Energia,ataque=ataque)

    def habla(self):
        ptint("hmmmmm...*")

    def propagar_enfermedad(self):
        print("El zoombie esta tratando de propagar la enfermedad!!!")

    def ataque_especial(self):
        print("zoombie ataque especial")
        funcion_ataque_especial=random.random() < 0.50
        if funcion_ataque_especial:
            self.puntos_energia += 2
            print("zoombie ha regenerado su energia con 2HP!")
            


        
        