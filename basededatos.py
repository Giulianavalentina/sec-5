import sqlite3

DATABASE = "sensor.sqlite"

def crear_bd():
    """Crear la base de datos y la tabla si no existen."""
    # Conectar a la base de datos (se creará si no existe)
    conexion = sqlite3.connect(DATABASE)
    
    # Crear un cursor para ejecutar las consultas
    cursor = conexion.cursor()

    # Código SQL para crear la tabla
    sql_crear_tabla = """
    CREATE TABLE IF NOT EXISTS valores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor_sensor INTEGER
    );
    """

    # Ejecutar la consulta para crear la tabla
    cursor.execute(sql_crear_tabla)

    # Confirmar los cambios
    conexion.commit()

    # Cerrar la conexión
    conexion.close()
    print(f"Base de datos '{DATABASE}' creada y tabla 'valores' inicializada.")

# Ejecutar la función para crear la base de datos y la tabla
if __name__ == '__main__':
    crear_bd()
