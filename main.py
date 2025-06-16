"Archivo de administrador de tareas"

tareas = []

def mostrarMenu():

    print("Menu del administrador")

    print("1. Ver tareas\n" \
    "2. Agregar nueva tarea\n" \
    "3. Marcar tarea como completada\n" \
    "4. Eliminar tarea\n" \
    "5. Salir")

def verTareas():
    print(tareas)

def agregarTareas():
    nuevaTarea = input("Escriba la tarea\n")
    tareas.append(nuevaTarea)

respuesta = ""
while respuesta != "5":

    mostrarMenu()

    respuesta = input("Seleccione la accion\n")
    
    if respuesta == "1":
        verTareas()
        
    elif respuesta == "2":
        agregarTareas()





menu()