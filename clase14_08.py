'''Trabajo de listas donde elimina los repetidos
lista=[1,2,3,4,"hola",2,2]
conjunto=set(lista)
lista=list(conjunto)
print(conjunto)'''

lista1 = [1,2,"miguel","angel","jose","camila",1,2]
lista2 = ["miguel","angel",1,2,3,4,"miguel","angel",]
print("listas:")
print(lista1)
print(lista2)
#imprimir: las dos listas (sin repeticiones)
print("\nimprimir: las dos listas (sin repeticiones)")
unity=set(lista1)
lista1=list(unity)
print(unity)
unity2=set(lista2)
lista2=list(unity2)
print(f"\n{unity2}\n")
#lista de palabras que aparecen en la primera lista
print("\nlista de palabras que aparecen en la primera lista")
print(unity)
#lista de palabras que aparecen en la segunda lista
print("\nlista de palabras que aparecen en la segunda lista")
print(f"\n{unity2}\n")
#lista de palabras que aparecen en ambas listas
print("lista de palabras que aparecen en ambas listas")
print(f"\nlistas combinadas{unity},{unity2}")
