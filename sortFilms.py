import os


def main():
    filmList = os.listdir("D:\Pobrane\Filmy")

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
    filmMessage = ""

    for film in filmList:
        filmName = convertName(film)

        filmDict[filmName] = str(filmCount)
        filmMessage = (
            filmMessage + numberDict.get(str(filmCount)) + " " + filmName + "\n"
        )
        filmCount += 1

    return filmDict, filmMessage


def convertName(filmName):
    filmFormat = ""
    for word in filmName.split("."):
        if word.isnumeric():
            filmFormat += word
            return filmFormat
        filmFormat += word + " "


if __name__ == "__main__":
    main()
