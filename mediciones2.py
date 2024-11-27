import sqlite3
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

DATABASE = "sensor.sqlite"

def obtener_bd():
    """Obtener la conexión a la base de datos."""
    db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row
    return db

def inicializar_bd():
    """Inicializar el esquema de la base de datos si no está configurado."""
    # Crear la base de datos si no existe
    if not os.path.exists(DATABASE):
        db = obtener_bd()
        with open("valores", "r") as f:
            db.executescript(f.read())
            db.commit()
        db.close()

@app.route('/')
def inicio():
    """Página principal que inicializa la base de datos."""
    inicializar_bd()
    return "Base de datos inicializada y aplicación en ejecución."

@app.route('/mediciones', methods=['POST'])
def mediciones():
    """Manejar la recepción de datos del sensor."""
    try:
        valor_str = request.form['medicion']
        valor = int(valor_str)  # Convertir el valor de string a entero

        # Insertar el valor en la base de datos
        db = obtener_bd()
        db.execute("INSERT INTO valores (valor_sensor) VALUES (?)", (valor,))
        db.commit()

        return jsonify({"estado": "exito", "mensaje": "Datos insertados correctamente"}), 200
    except Exception as e:
        return jsonify({"estado": "error", "mensaje": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
