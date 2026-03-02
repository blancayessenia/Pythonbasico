from Enemigo import *
from zoombie import *
from ogro import *

zoombie = zoombie(10, 1)
ogro = ogro (20, 3)

def batalla(e1: Enemigo, e2: Enemigo):
    e1.habla()
    e2.habla()

while e1.puntos_energia > 0 and e2.puntos_energia > 0:
    print("##############")
    e1.ataque_especial()
    e2.ataque_especial()
    print(f"{e1.get_tipo_enemigo()}:quedan: {e1.puntos_energia}puntos de energia")
    print(f"{e2.get_tipo_enemigo()}:quedan: {e2.puntos_energia}puntos de energia")
    print(f"Ataque: {e2.ataque}")
    e1.puntos_energia -= e2.ataque
    print("==========")
    print(f"ataque: {e1.ataque}")
    e2.puntos_energia -= e1.ataque

print("###############")
if e1.puntos_energia > 0:
    print(f"{e1.get_tipo_enemigo()}gano!!!!")

else:
    print(f"{e2.get_tipo_enemigo()}gano!!!!")
   
print("==========BATALLA==========")
batalla(zoombie, ogro)
print("==========FIN DE LA BATALLA==========")
#print(f"{zoombie.get_tipo_Enemigo()}tiene {zoombie.puntos_energia}de energia y ataca con {zoombie.ataque}")
#print(f"{ogro.get_tipo_Enemigo()}tiene{ogro.puntos_energia}de energia y ataca con{ogro.ataque}")
