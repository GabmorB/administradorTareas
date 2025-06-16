# Administrador de Tareas - Proyecto 1

Este proyecto es parte de una serie de ejercicios para reforzar y profundizar en los conocimientos adquiridos tras completar el libro *Python Crash Course*.

## ✨ Objetivo

Construir una aplicación de consola que permita gestionar tareas de forma interactiva, integrando buenas prácticas de programación, control de flujo y uso de listas en Python, además de aplicar control de versiones con Git y GitHub.

---

## 📅 Actividades realizadas

### 1. **Inicialización del Proyecto**

* Definición del objetivo general.
* Estructura base del programa con funciones y ciclo `while`.

### 2. **Configuración de Git y GitHub con SSH**

* Creación de repositorio local con `git init`.
* Generación y registro de clave SSH.
* Enlace con repositorio remoto usando:

  ```bash
  git remote add origin git@github.com:GabmorB/administradorTareas.git
  ```
* Resolución de errores de autenticación (403, publickey).

### 3. **Desarrollo del Menú Interactivo**

* Menú principal con opciones:

  1. Ver tareas
  2. Agregar tarea
  3. Marcar como completada
  4. Eliminar tarea
  5. Salir
* Uso de `input()` para interacción.
* Uso de listas y funciones.
* Depuración de problema de visualización usando pausa:

  ```python
  input("Presiona Enter para continuar...")
  ```

---

## 📃 Conceptos de Python utilizados

| Concepto       | Descripción                                  |
| -------------- | -------------------------------------------- |
| `while`        | Bucle que mantiene activo el menú            |
| `input()`      | Entrada del usuario                          |
| `append()`     | Agregar elementos a una lista                |
| `if/elif/else` | Control de flujo según selección del usuario |
| `print()`      | Salida en consola                            |
| `def`          | Declaración de funciones                     |

## 🚀 Conceptos de Git/GitHub trabajados

| Comando                   | Propósito                                          |
| ------------------------- | -------------------------------------------------- |
| `git init`                | Inicializa repositorio local                       |
| `git add .`               | Agrega archivos al área de staging                 |
| `git commit -m "mensaje"` | Crea un snapshot del estado actual del proyecto    |
| `git remote add origin`   | Enlaza el repo local con GitHub                    |
| `git push -u origin main` | Sube los cambios a GitHub                          |
| `ssh-keygen`              | Genera clave SSH                                   |
| `ssh-add`                 | Agrega la clave privada al agente de autenticación |
| `git pull`                | Trae cambios del repositorio remoto                |

---

## 📆 Estado actual

* [x] Proyecto iniciado
* [x] Git y GitHub configurados correctamente con SSH
* [x] Menú funcional para ver y agregar tareas
* [ ] Marcar tareas como completadas
* [ ] Eliminar tareas
* [ ] Mejoras en la presentación de la consola

---

## 🙌 Próximos pasos

* Implementar las opciones 3 y 4 del menú.
* Guardar las tareas en un archivo de texto o JSON.
* Refactorizar para separar lógica en módulos.
* Escribir pruebas básicas.

"Agrego resumen del proyecto"
