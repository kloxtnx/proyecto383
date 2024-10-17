import mysql.connector
from mysql.connector import Error

def miConexionDb():

# utilizo try para manejar los errores
    try:

        # Establesco la conexion 
        conexion = mysql.connector.connect(
            user='uihdvgvu2vlndceu',password='5sTqrqljQ97tld9LBDAf',
            host='byqgtgv9qu7jixdao2sl-mysql.services.clever-cloud.com',
            database='byqgtgv9qu7jixdao2sl',
            port='3306'
        )

        # valido si la conexion fue exitosa
        if conexion.is_connected():
            print('conexion establecida correctamente')
            return conexion
            
    except Error as e:
        # Si ocurre un error en el bloque try, este código se ejecuta
         print(f"Error al conectarse a la base de datos: {e}")
         return None









