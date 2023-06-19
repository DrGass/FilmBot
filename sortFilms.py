import os
from database import save, load
import psycopg2
from dbconfig import config
from psycopg2.extras import Json

# Think of a way to imporove that because it's kinda wacky :>
def main():

    numberDict = {
        "1": ":one:",
        "2": ":two:",
        "3": ":three:",
        "4": ":four:",
        "5": ":five:",
        "6": ":six:",
        "7": ":seven:",
        "8": ":eight:",
        "9": ":nine:",
    }

    filmCount = 1
    filmDict = {}
    load(id,['films'])
    filmMessage = ""

    for film,watched in filmDict.items:
        if watched == 1:
            continue
        filmMessage = (
            filmMessage + numberDict.get(str(filmCount)) + " " + film + "\n"
        )
        filmCount += 1
    print (filmDict,filmMessage)
    return filmDict, filmMessage


if __name__ == "__main__":
    main()
