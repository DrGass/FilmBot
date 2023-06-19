import os
from database import save, load
import psycopg2
from dbconfig import config
from psycopg2.extras import Json

dict = {
        'baton' : 2,
        'kutas' : 2
        }

dict2 = {
    'anarchia' : 3,
    'penis' : 6,
    'kutas' : 8
}

# counting time
from timeit import default_timer as timer

# Start timer
start = timer()

dict.update(dict2)

# End timer
end = timer()
print(end - start)
print(dict)


#example of putting dict in db
dict = {
    "Jan" : 0,
    "Paweł": 2
}

def save(id):
    """ Save all the data to database """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()

        # select_query = cur.execute(f'SELECT * FROM guilds WHERE id = {id};')
        cur.execute(f"UPDATE guilds SET films = {Json(dict)} WHERE id = 420313740916031499;")
        data = cur.fetchone()

        print(data[0],type(data[0]))

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')