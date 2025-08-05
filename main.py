"Archivo de administrador de tareas"

import json
import os

tareas = {}
if os.path.exists('salida.json'):
    try:
        with open('salida.json', 'r') as j:
            tareas = json.load(j)
    except json.JSONDecodeError:
        print("Advertencia: el archivo está vacío o corrupto. Se iniciará con tareas vacías.")


def mostrarMenu():

    print("Menu del administrador")

    print("1. Ver tareas\n" \
    "2. Agregar nueva tarea\n" \
    "3. Marcar tarea como completada\n" \
    "4. Eliminar tarea\n" \
    '5. Guardar actividad\n' \
    "6. Salir")

def verTareas():
    print(tareas)

def agregarTareas():
    nuevaTarea = input("Escriba la tarea\n")
    tareas[nuevaTarea] = 'pendiente'

def tareasCompletadas():
    tareaCompletada = input("Escriba la tarea completada\n")
    tareas[tareaCompletada] = 'Completada'

def eliminarTarea():
    tareaEliminada = input("Escriba la tarea a eliminar\n")
    del tareas[tareaEliminada]

def guardarActividad():
    with open('salida.json', 'w') as f:
        json.dump(tareas, f, indent=4)

respuesta = ""
while respuesta != "6":

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
        respuesta = input('¿Desea eliminar esta actividad? (s/n)')
        respuesta_min = respuesta.lower()
        if respuesta_min == 's':
            eliminarTarea()
        else:
            continue
        verTareas()

    elif respuesta == "5":
        guardarActividad()
