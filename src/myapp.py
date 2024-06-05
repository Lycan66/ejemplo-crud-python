import psycopg2

def insertarCategoria(id,nombre):
    cursor = conexion.cursor()
    sentencia = "INSERT INTO categoria VALUES (%s, %s)"
    
    valores = (id,nombre)
    cursor.execute(sentencia, valores)
    conexion.commit()
    conexion.close()

def traterTodo():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categoria")
    resultado = cursor.fetchall()

    for fila in resultado:
        print(fila)
    conexion.close()

def modificarRegistro(id, nuevoNombre):
    cursor = conexion.cursor()
    sentencia = "UPDATE categoria SET nombre = %s WHERE codigo = %s"
    valores = (nuevoNombre, id)
    cursor.execute(sentencia, valores)

    conexion.commit()
    conexion.close()

def eliminarRegistro(id):
    cursor = conexion.cursor()
    sentencia = "DELETE FROM categoria WHERE codigo = %s"

    cursor.execute(sentencia, (id,))
    conexion.commit()
    conexion.close()

def consultarPorId(id):
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM categoria WHERE codigo = %s"
    cursor.execute(sentencia, (id,))
    print(cursor.fetchone())

    conexion.close()

def ordenarAsc():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categoria ORDER BY nombre ASC")
    resultado = cursor.fetchall()

    for fila in resultado:
        print(fila)

    conexion.close()

def ConsultaMultitabla():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM producto INNER JOIN categoria ON producto.categoria = categoria.codigo")
    resultado = cursor.fetchall()

    for fila in resultado:
        print(fila)
    
    conexion.close()

try:
    conexion = psycopg2.connect(
        database = "Lavadero",
        user = "postgres",
        password = "p123",
        host = "localhost",
        port = "5432"
    )
    ConsultaMultitabla()
    #ordenarAsc()
    #consultarPorId(2)
    #eliminarRegistro(2)
    #modificarRegistro(1, "Literatura")
    #traterTodo()
    #insertarCategoria(2,"Mascotas")
except psycopg2.DatabaseError as e:
    print(e)