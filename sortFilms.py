import os
from database import save, load
import psycopg2
from dbconfig import config
from psycopg2.extras import Json


# Check if this cannot be written better because it looks cursed XD
def main(id):
    number_dict = {
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

    film_count = 1
    film_dict = load(id, ["films"])[0]
    film_message = ""

    for film, watched in film_dict.items:
        if watched == 1:
            continue
        film_message = film_message + number_dict.get(str(film_count)) + " " + film + "\n"
        film_count += 1
    print(film_dict, film_message)
    return film_dict, film_message


if __name__ == "__main__":
    main()
