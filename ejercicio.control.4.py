"""
Ejercicio control 4

"""
print("----------------Registro de visitantes-----------------")

def registro_visitantes_por_sala (sala): # Creamos una funcion para el registro de visitantes por sala
    visitantes = set() # Declaramos que los visitantes son un conjunto (set)
    print(f"Ingresa los nombres de los visitantes de la {sala}")
    while True: 
        nombre = str(input("Nombre: ")) # Ingreso de nombre
        if nombre == "finalizar": # Si el nombre es finalizar, se termina el registro de nombres
            break
        else:
            visitantes.add(nombre) # Se añade el nombre al set
    return visitantes

sala1 = registro_visitantes_por_sala("Sala 1") # Se crea una variable de cada sala y se le da como parametro el nombre de la sala
sala2 = registro_visitantes_por_sala("Sala 2")
sala3 = registro_visitantes_por_sala("Sala 3")

total_visitantes = sala1.union(sala2, sala3) # Unimos las tres salas

print("Los nombres de los visitantes son: ") 
for nombre in (total_visitantes):
    print(f"{nombre}")

print(f"La cantidad de la sala 1 son: {len(sala1)} personas. ")
print(f"La cantidad de la sala 2 son: {len(sala2)} personas. ")
print(f"La cantidad de la sala 3 son: {len(sala3)} personas. ")


