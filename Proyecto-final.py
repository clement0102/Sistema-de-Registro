# Registro Académico de Estudiantes

# ==========================================
# PROYECTO FINAL: Sistema de Registro Académico
# Asignatura: Programación Estructurada
# Estudiante: [Escribe tu nombre completo aquí]
# ==========================================

# PASO 1: Estructura de Datos
estudiantes = []

print("=" * 50)
print("   SISTEMA DE REGISTRO DE CALIFICACIONES")
print("=" * 50)
print("¡Bienvenido al sistema académico!")
print("Se registrarán 3 estudiantes.")
print("Las notas deben estar entre 0 y 100.")
print("La nota mínima para aprobar es 60.")
print("=" * 50)

# Registro de 3 estudiantes
for i in range(3):

    print(f"\n--- Ingresando datos del Estudiante {i + 1} ---")

    nombre = input("Nombre y Apellido: ")

    # PASO 2: Validaciones
    try:
        nota1 = float(input("Nota del Parcial 1: "))
        nota2 = float(input("Nota del Parcial 2: "))

        if not (0 <= nota1 <= 100):
            print("Nota del Parcial 1 fuera de rango. Se asignará 0.")
            nota1 = 0.0

        if not (0 <= nota2 <= 100):
            print("Nota del Parcial 2 fuera de rango. Se asignará 0.")
            nota2 = 0.0

    except ValueError:
        print("Error: ingresaste un valor no válido.")
        print("Se asignará 0 a ambas notas.")
        nota1 = 0.0
        nota2 = 0.0

    # Cálculo de la nota final
    nota_final = (nota1 + nota2) / 2

    # Guardar datos
    estudiantes.append([nombre, nota1, nota2, nota_final])


# PASO 3: Reporte final
print("\n" + "=" * 70)
print("                  REPORTE FINAL DE ESTUDIANTES")
print("=" * 70)

for alumno in estudiantes:

    nombre_alumno = alumno[0]
    nota1 = alumno[1]
    nota2 = alumno[2]
    promedio = alumno[3]

    # Estado académico
    if promedio < 60:
        estado = "REPROBADO"
    else:
        estado = "APROBADO"

    # Escala de aprendizaje
    if promedio < 60:
        escala = "AI"
    elif promedio <= 75:
        escala = "AF"
    elif promedio <= 89:
        escala = "AS"
    else:
        escala = "AA"

    print(f"\nEstudiante: {nombre_alumno}")
    print(f"Parcial 1: {nota1:.2f}")
    print(f"Parcial 2: {nota2:.2f}")
    print(f"Nota final: {promedio:.2f}")
    print(f"Estado académico: {estado}")
    print(f"Escala de aprendizaje: {escala}")

print("\n" + "=" * 70)
print("                    FIN DEL REPORTE")
print("=" * 70)