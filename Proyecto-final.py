#Sistema de Registro Académico

# ==========================================
# PROYECTO FINAL: Sistema de Registro Académico
# Asignatura: Programación Estructurada
# Estudiante: [Escribe tu nombre completo aquí]
# ==========================================

# PASO 1: Estructura de Datos
# Lista vacía para guardar los datos de todos los alumnos
estudiantes = []

print("=" * 50)
print("   SISTEMA DE REGISTRO DE CALIFICACIONES")
print("=" * 50)
print("¡Bienvenido al sistema académico!")
print("Se registrarán 3 estudiantes.")
print("Las notas deben estar entre 0 y 100.")
print("La nota mínima para aprobar es 60.")
print("=" * 50)

# Utilizamos un ciclo for para registrar a 3 estudiantes
for i in range(3):

    print(f"\n--- Ingresando datos del Estudiante {i + 1} ---")

    nombre = input("Nombre y Apellido: ")

    # PASO 2: Validaciones
    # Utilizamos try-except para evitar errores al ingresar las notas
    try:
        nota1 = float(input("Nota del Parcial 1: "))
        nota2 = float(input("Nota del Parcial 2: "))

        # Validamos que las notas estén entre 0 y 100
        if not (0 <= nota1 <= 100):
            print("La nota del Parcial 1 está fuera de rango. Se asignará 0.")
            nota1 = 0.0

        if not (0 <= nota2 <= 100):
            print("La nota del Parcial 2 está fuera de rango. Se asignará 0.")
            nota2 = 0.0

    except ValueError:
        print("Error: Ingresaste un valor no válido.")
        print("Se asignará 0 a ambas notas.")
        nota1 = 0.0
        nota2 = 0.0

    # Calculamos la nota final
    nota_final = (nota1 + nota2) / 2

    # Guardamos los datos del estudiante en nuestra lista principal
    estudiantes.append([nombre, nota1, nota2, nota_final])


# PASO 3: Evaluación de Resultados
print("\n" + "=" * 60)
print("             REPORTE FINAL DE ESTUDIANTES")
print("=" * 60)

for alumno in estudiantes:

    # Extraemos los datos de la lista
    nombre_alumno = alumno[0]
    promedio = alumno[3]

    estado = ""

    # PASO 4: Condicionales lógicos
    # < 60 = Reprobado | > 95 = Sobresaliente | El resto = Aprobado

    if promedio < 60:
        estado = "REPROBADO"
    elif promedio > 95:
        estado = "SOBRESALIENTE"
    else:
        estado = "APROBADO"

    print(f"Estudiante: {nombre_alumno} | "
          f"Promedio: {promedio:.2f} | "
          f"Estado: {estado}")

print("\n" + "=" * 60)
print("                  FIN DEL REPORTE")
print("=" * 60)