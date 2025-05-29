from flask import Flask, render_template, request, redirect, url_for

import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'Estudiantes'
}


# TODO -> QUITAR LOS ESTATICOS 
listaEstudiantes = []

listaNotas = []

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/estudiantes')
def estudiantes():
    # Conexión a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM Estudiante"
    cursor.execute(query)
    estudiantes = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("estudiantes.html", data = estudiantes)

@app.route('/registrar')
def registrar():
    return render_template("registrar.html")

@app.route("/registrar", methods=['POST'])
def enviar_datos():
   
    if request.method == 'POST':
        id = request.form['Id']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        matematicas = request.form['mate']
        ingles = request.form['ingles']
        espa = request.form['espa']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "Insert into Estudiante (Id, Nombre, Apellido) values (%s, %s, %s)"
        values = (id, nombre, apellido)
        query2 = "Insert into Notas (Id, Matematicas, Español, Ingles) values (%s, %s, %s, %s)"
        values2 = (id, matematicas, espa, ingles)
        cursor.execute(query, values)
        cursor.execute(query2, values2)
        conn.commit()
        cursor.close()
        conn.close()
  
  # TODO -> Guardar esta información en los arreglos

    return redirect(url_for('estudiantes'))

@app.route('/Notas')
def Notas():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT e.Id, e.Nombre, e.Apellido, n.Matematicas, n.Español, n.Ingles FROM Estudiante AS e INNER JOIN Notas AS n ON e.Id = n.Id"
    cursor.execute(query)
    estudiantes_notas_raw = cursor.fetchall()

    # Obtener todos los estudiantes para el select
    queryEstudiantes = "SELECT Id, Nombre, Apellido FROM Estudiante"
    cursor.execute(queryEstudiantes)
    estudiantes = cursor.fetchall()

    cursor.close()
    conn.close()

    estudiantes_notas_con_promedio = []
    for fila in estudiantes_notas_raw:
        try:
            matematicas = float(fila[3])
            espanol = float(fila[4])
            ingles = float(fila[5])
            promedio_individual = (matematicas + espanol + ingles) / 3
        except (ValueError, TypeError):
            promedio_individual = 0.0
        
        estudiantes_notas_con_promedio.append(list(fila) + [promedio_individual])

    return render_template("notasEstudiante.html", consulta=estudiantes_notas_con_promedio, estu=estudiantes)


# Funcionalidad completa del filter

@app.route('/Notas', methods=['POST'])
def Filtar():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    if request.method == 'POST':
        estudiante_id = request.form['filtro']

        print("ID ESTUDIANTE: ", estudiante_id)

        # Obtener todos los estudiantes para poblar el select (importante para que el filtro siga funcionando)
        queryEstudiantes = "SELECT Id, Nombre, Apellido FROM Estudiante"
        cursor.execute(queryEstudiantes)
        estudiantes = cursor.fetchall()

        # Obtener los datos del estudiante y sus notas
        query = "SELECT e.Id, e.Nombre, e.Apellido, n.Matematicas, n.Español, n.Ingles FROM Estudiante AS e INNER JOIN Notas AS n ON e.Id = n.Id WHERE e.Id = %s"
        cursor.execute(query, (estudiante_id,))
        notas_raw = cursor.fetchall()

        cursor.close()
        conn.close()

        notas_con_promedio = []
        for fila in notas_raw:
            try:
                matematicas = float(fila[3])
                espanol = float(fila[4])
                ingles = float(fila[5])
                promedio_individual = (matematicas + espanol + ingles) / 3
            except (ValueError, TypeError):
                promedio_individual = 0.0 # Manejo de error si las notas no son números
            notas_con_promedio.append(list(fila) + [promedio_individual])

        return render_template("notasEstudiante.html", consulta=notas_con_promedio, estu=estudiantes)
    return redirect(url_for('Notas'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        matematicas = request.form['matematicas']
        espanol = request.form['espanol']
        ingles = request.form['ingles']
        cursor.execute("UPDATE Estudiante SET Nombre=%s, Apellido=%s WHERE Id=%s", (nombre, apellido, id))
        cursor.execute("UPDATE Notas SET Matematicas=%s, Español=%s, Ingles=%s WHERE Id=%s", (matematicas, espanol, ingles, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('Notas'))
    else:
        cursor.execute("SELECT * FROM Estudiante WHERE Id=%s", (id,))
        estudiante = cursor.fetchone()
        cursor.execute("SELECT * FROM Notas WHERE Id=%s", (id,))
        notas = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('editar.html', estudiante=estudiante, notas=notas)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Notas WHERE Id=%s", (id,))
    cursor.execute("DELETE FROM Estudiante WHERE Id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('Notas'))

if __name__ == '__main__':
    app.run(debug=True)