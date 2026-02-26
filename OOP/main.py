from Enemigo import *
from zoombie import *
from ogro import *

zoombie = zoombie(10, 1)
ogro = ogro (20, 3)

print(f"{zoombie.get_tipo_Enemigo()}tiene {zoombie.puntos_energia}de energia y ataca con {zoombie.ataque}")
print(f"{ogro.get_tipo_Enemigo()}tiene{ogro.puntos_energia}de energia y ataca con{ogro.ataque}")
