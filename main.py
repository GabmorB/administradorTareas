"Archivo de administrador de tareas"

tareas = []
completadas = []

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

def tareasCompletadas():
    tareaCompletada = input("Escriba la tarea completada\n")
    completadas.append(tareaCompletada)
    print("Tareas completadas", completadas)

def eliminarTarea():
    tareaEliminada = input("Escriba la tarea a eliminar\n")
    tareas.remove(tareaEliminada)

respuesta = ""
while respuesta != "5":

    mostrarMenu()

    respuesta = input("Seleccione la accion\n")
    
    if respuesta == "1":
        print("Las tareas son:")
        verTareas()
        
    elif respuesta == "2":
        agregarTareas()
        verTareas()

    elif respuesta == "3":
        tareasCompletadas()

    elif respuesta == "4":
        eliminarTarea()
        verTareas()
