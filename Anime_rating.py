import pandas

def Main():
    anime = pandas.read_csv("anime.csv")
    anime = No_Hentai(anime)

# Remove bad animes that people shouldn't watch.
def No_Hentai(file):
    good_rows = []
    count = -1
    rows = [list(row) for row in file.values]
    for colums in rows:
        #Creates a list of all the anime data
        good_rows.append(colums)
        count += 1
        if colums[2] == "genre":
            pass
        else:
            #removes animes with problimatic genres from the list
            separate_generes = colums[2].split()
            for x in separate_generes:
                if x == "Hentai" or x == "Hentai,":
                    good_rows.pop(count)
                    count = count - 1
                else:
                    pass
    return good_rows