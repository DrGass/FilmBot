import psycopg2
from dbconfig import config
from psycopg2.extras import Json


def load(id, queryList):
    """Save all the data to database"""
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        # create a cursor

        cur = conn.cursor()
        query = ""
        for item in queryList:
            query += str(item) + ","

        # select_query = cur.execute(f'SELECT * FROM guilds WHERE id = {id};')
        cur.execute(f"SELECT {query[:-1]} FROM guilds WHERE id = {id};")
        data = cur.fetchall()

        print(data, type(data))

        # close the communication with the PostgreSQL
        cur.close()

        return data

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def save(id, queryDict):
    """Load all the data from database"""
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        for query, value in queryDict.items():
            try:
                cur.execute(f"UPDATE guilds SET '{str(query)}' = {value} WHERE id = {id};")
            except:
                print('oopsie daisy')

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def main():
    query = ["films", "winner"]
    pp = load(420313740916031499, query)
    print(pp)


if __name__ == "__main__":
    main()
