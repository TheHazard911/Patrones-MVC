import sqlite3

class Modelo():
    def obtener_datos(self):
        try:
            # Crea una conexión a la base de datos
            with sqlite3.connect("MVC/db/plantilla.db") as conn:
                cursor = conn.cursor()

            # Ejecuta una consulta SELECT en la tabla deseada
                cursor.execute("SELECT * FROM prueba")
                resultados = cursor.fetchall()

            # Imprime los resultados (puedes adaptarlo según tus necesidades)
                for fila in resultados:
                    # print(fila)
                    return fila

        except sqlite3.Error as e:
            print(f"Error al obtener datos: {e}")
        

#---------------------para hacer la instancia-----------------
# modelo = Modelo()
# modelo.obtener_datos()