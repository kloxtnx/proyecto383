from db_connection import get_conecction

def fetch_terceros():
    connection = get_conecction

    if connection is None:
        print('no se pudo conectar a la base de datos.')
        return
    
    try:
        cursor = connection.cursor()

        query = 'SELECT * FROM TERCEROS'

        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            print(row)
