
from flask import Flask, render_template
from modules import reportes, aire, censo , educacion, movilidad

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reportes')
def modulo_reportes():
    return reportes.mostrar_reportes()

@app.route('/aire')
def modulo_aire():
    return aire.mostrar_aire()

@app.route('/censo')
def modulo_censo():
    return censo.mostrar_censo()

@app.route('/educacion')
def modulo_educacion():
    return educacion.mostrar_educacion()

@app.route('/movilidad')
def modulo_movilidad():
    return movilidad.mostrar_movilidad()


if __name__ == '__main__':
    app.run(debug=True)
# This is a simple Flask application that returns "Hello, Flask!" when accessed at the root URL.
# To run this application, save it as app.py and execute it using the command:
# python app.py
# Make sure you have Flask installed in your Python environment. You can install it using pip:
# pip install Flask
# After running the application, you can access it in your web browser at http://
# localhost:5000/
# or http://
