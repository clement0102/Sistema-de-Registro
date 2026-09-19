# ==========================================
# PROYECTO FINAL: Sistema de Registro Académico
# Asignatura: Programación Estructurada
# Estudiante: [Escribe tu nombre completo aquí]
# ==========================================

# PASO 1: Estructura de Datos
# Lista vacía para guardar los datos de todos los alumnos
estudiantes = []

print("--- SISTEMA DE REGISTRO DE CALIFICACIONES ---")

# Utilizamos un ciclo for para registrar a 3 estudiantes
for i in range(3):
    print(f"\n--- Ingresando datos del Estudiante {i+1} ---")
    nombre = input("Nombre y Apellido: ")
    
    # PASO 2: Validaciones
    # INSTRUCCIÓN: Utiliza try-except para pedir las notas y evitar errores.
    # ---> INICIO DE TU CÓDIGO <---
    try:
        # Pide la nota del parcial 1 y parcial 2 aquí (recuerda usar float)
        # nota1 = ...
        # nota2 = ...
        pass # Borra este 'pass' cuando escribas tu código
        
    except ValueError:
        print("Error: Ingresaste un valor no válido. Se asignará 0 a ambas notas.")
        nota1 = 0.0
        nota2 = 0.0
    # ---> FIN DE TU CÓDIGO <---

    # Calculamos la nota final
    nota_final = (nota1 + nota2) / 2
    
    # Guardamos los datos del estudiante en nuestra lista principal
    estudiantes.append([nombre, nota1, nota2, nota_final])


# PASO 3: Evaluación de Resultados
print("\n==========================================")
print("REPORTE FINAL DE ESTUDIANTES")
print("==========================================")

for alumno in estudiantes:
    # Extraemos los datos de la lista
    nombre_alumno = alumno[0]
    promedio = alumno[3]
    
    estado = ""
    # PASO 4: Condicionales lógicos
    # INSTRUCCIÓN: Utiliza if, elif, else para determinar el estado del alumno.
    # < 60 = Reprobado | > 95 = Sobresaliente | El resto = Aprobado.
    # ---> INICIO DE TU CÓDIGO <---
    
    # Escribe tus condiciones aquí
    
    # ---> FIN DE TU CÓDIGO <---

    print(f"Estudiante: {nombre_alumno} | Promedio: {promedio:.2f} | Estado: {estado}")