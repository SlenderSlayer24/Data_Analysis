import pandas

def Main():
    anime = pandas.read_csv("anime.csv")
    anime = No_Hentai(anime)
    Episode_Counter(anime)

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

def Episode_Counter(anime):
    avarage = 0
    episode_count = 0
    series_count = 0
    for row in anime:
        if row[4] == "Unknown":
            pass
        elif row[3] == "Movie":
            pass
        else:
            episode_count += int(row[4])
            series_count += 1
    avarage = episode_count/series_count
    print()
    print(f"The total number of anime series is {series_count}.")
    print(f"The total number of episodes in every anime is {episode_count}.")
    print(f"The avarage number of anime episodes for all animes is {round(avarage)}.")
    print()

Main()