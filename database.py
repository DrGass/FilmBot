import psycopg2
from dbconfig import config

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

        select_query = cur.execute(f'SELECT * FROM guilds WHERE id = {id};')
        data = cur.fetchone()

        print(data)

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def load(id):
    """ Load all the data from database """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()

        try:
            select_query = cur.execute(f'SELECT * FROM guilds WHERE id = {id};')
            data = cur.fetchone()
            return data
        except:
            cur.execute(f'INSERT INTO guilds(id) VALUES({id})')
        
    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def main():
    save(1)


if __name__ == "__main__":
    main()


