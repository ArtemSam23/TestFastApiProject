import psycopg2
from db_config import config
from pprint import pprint


def connect_to_db():
    connection = None
    try:
        params = config()
        print('Connecting to PostgreSQL database ...')
        connection = psycopg2.connect(**params)
        print('Successfully connected to PostgreSQL database.')
        pprint(params)

        # create cursor
        cursor = connection.cursor()

        print('PostgreSQL database version: ')
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(*db_version)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')


if __name__ == '__main__':
    connect_to_db()
