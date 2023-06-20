import psycopg2
from dbconfig import config
from psycopg2.extras import Json
import os

# At the moment it's hardcoded for my id and dir, gonna change that to integration with website(more like desktop app) where You can add it for Your server specifically

def convertName(filmName):
    filmFormat = ""
    for word in filmName.split("."):
        if word.isnumeric():
            filmFormat += word
            return filmFormat
        filmFormat += word + " "


def createDict():
    filmList = os.listdir("..\\Filmy\\")
    filmDict = {}

    for film in filmList:
        try:
            filmDict[str(convertName(film))] = 0
        except:
            print("oopsie, coś sie zjebao")
    return filmDict


def main():
    """Save all the data to database"""
    id = 420313740916031499
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # Create dict of Films to watch
        newDict = createDict()

        cur.execute(f"SELECT films FROM guilds WHERE id = {id};")
        oldDict = cur.fetchone()
        if oldDict[0] is not None:
            newDict.update(oldDict[0])
            print(newDict, "\n", oldDict)

        # Put new list to db
        cur.execute(f"UPDATE guilds SET films = {Json(newDict)} WHERE id = {str(id)};")
        conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    main()
