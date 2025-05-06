# Listas para almacenar los datos
estudiantes = []
cursos = ["Matemáticas", "Física", "Química", "Literatura"]  # Cursos disponibles
inscripciones = []  # Lista de tuplas (id_estudiante, curso)

def registrar_estudiante():
    id_est = input("Ingrese identificador del estudiante: ").strip()
    # Verificar que no exista un estudiante con ese id
    for e in estudiantes:
        if e['id'] == id_est:
            print("Ya existe un estudiante con ese identificador.")
            return
    nombre = input("Ingrese nombre completo: ").strip()
    correo = input("Ingrese correo electrónico: ").strip()
    estudiantes.append({'id': id_est, 'nombre': nombre, 'correo': correo})
    print("Estudiante registrado correctamente.")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("Estudiantes registrados:")
    for e in estudiantes:
        print(f"{e['id']}: {e['nombre']} ({e['correo']})")

def mostrar_cursos():
    print("Cursos disponibles:")
    for idx, c in enumerate(cursos, start=1):
        print(f"{idx}. {c}")

def inscribir_estudiante_curso():
    id_est = input("Ingrese identificador del estudiante para inscribir: ").strip()
    # Verificar si existe
    estudiante = None
    for e in estudiantes:
        if e['id'] == id_est:
            estudiante = e
            break
    if estudiante is None:
        print("Estudiante no encontrado.")
        return
    mostrar_cursos()
    opcion = input("Seleccione número del curso para inscribir: ").strip()
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(cursos):
        print("Curso inválido.")
        return
    curso_sel = cursos[int(opcion) - 1]
    # Verificar si ya está inscrito
    if (id_est, curso_sel) in inscripciones:
        print(f"El estudiante ya está inscrito en {curso_sel}.")
        return
    inscripciones.append((id_est, curso_sel))
    print(f"Estudiante {estudiante['nombre']} inscrito en {curso_sel}.")

def listar_cursos_estudiante():
    id_est = input("Ingrese identificador del estudiante para listar cursos: ").strip()
    # Verificar si existe
    estudiante = None
    for e in estudiantes:
        if e['id'] == id_est:
            estudiante = e
            break
    if estudiante is None:
        print("Estudiante no encontrado.")
        return
    cursos_est = [curso for (idest, curso) in inscripciones if idest == id_est]
    if not cursos_est:
        print(f"El estudiante {estudiante['nombre']} no está inscrito en ningún curso.")
    else:
        print(f"Cursos en los que está inscrito {estudiante['nombre']}:")
        for c in cursos_est:
            print(f"- {c}")

def eliminar_inscripcion():
    id_est = input("Ingrese identificador del estudiante para eliminar inscripción: ").strip()
    # Verificar si existe
    estudiante = None
    for e in estudiantes:
        if e['id'] == id_est:
            estudiante = e
            break
    if estudiante is None:
        print("Estudiante no encontrado.")
        return
    cursos_est = [curso for (idest, curso) in inscripciones if idest == id_est]
    if not cursos_est:
        print("El estudiante no tiene inscripciones para eliminar.")
        return
    print("Cursos inscritos:")
    for idx, c in enumerate(cursos_est, start=1):
        print(f"{idx}. {c}")
    opcion = input("Seleccione número del curso a eliminar inscripción: ").strip()
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(cursos_est):
        print("Opción inválida.")
        return
    curso_sel = cursos_est[int(opcion) - 1]
    inscripciones.remove((id_est, curso_sel))
    print(f"Inscripción en {curso_sel} eliminada para el estudiante {estudiante['nombre']}.")

def menu():
    while True:
        print("\n--- Menú de la aplicación ---")
        print("1. Registrar estudiante")
        print("2. Inscribir estudiante en curso")
        print("3. Listar cursos de un estudiante")
        print("4. Eliminar inscripción de estudiante")
        print("5. Mostrar estudiantes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            inscribir_estudiante_curso()
        elif opcion == "3":
            listar_cursos_estudiante()
        elif opcion == "4":
            eliminar_inscripcion()
        elif opcion == "5":
            mostrar_estudiantes()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()