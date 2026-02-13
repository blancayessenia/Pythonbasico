#loops

mi_lista = [1,2,3,4,5]
for i in mi_lista:
    print("el numero es:", i)

resultado = 0
for i in mi_lista:
    resultado += i

print("El resultado de la suma de mi lista es: {resultado}")

for i in range(2,8):
    print(i)

mi_lista_2 = ["lunes", "martes", "miercoles","jueves","viernes"]

for i in mi_lista_2:
    if i != "lunes":
        print(f"feliz{i}!")

# while loop
i=0

while i < 5:
    i += 1
    if i== 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i es ahora mayor o igual a 5")

# practica 2 
# dada la lista mi_lista_2 = ["lunes", "martes", "miercoles","jueves","viernes"]
# imprimir cada elemento de la lista tres veces y cuando sea lunes no lo incluyas 
# pista: usados dos tipos loops while y for en el mismo programa para hacerlo
# resultado:
# martes
# miercoles
# jueves
# viernes 
# martes
# miercoles
# jueves 
# viernes 
# martes
# miercoles
# jueves 
# viernes

mi_lista_2=  ["lunes", "martes", "miercoles","jueves","viernes"]

contador = 0
while contador < 3:
    for dia in mi_lista_2:
        if dia != "lunes":
            print(dia)
    contador += 1
    