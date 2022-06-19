import psycopg2
from psycopg2 import connect

global cursor, connection


class Response:
    def __init__(self, columns, data, error):
        self.columns = columns
        self.data = data
        self.error = error


def open_connection():
    global cursor, connection
    connection = connect(
        dbname='study',
        user='postgres',
        host='localhost',
        port='5554',
        password='password'
    )
    cursor = connection.cursor()


def execute_query(query):
    open_connection()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        column_names.__sizeof__()
        close_connection()
        return Response(column_names, result, '')
    except psycopg2.Error as e:
        close_connection()
        if e.args.__contains__('no results to fetch'):
            return Response('result', 'Operation was successful', '')
        return Response('', '', e.args)
    except RuntimeError:
        close_connection()
        return Response('', '', 'Internal server exception')


def close_connection():
    global cursor, connection
    connection.commit()
    cursor.close()
    connection.close()
