import pandas

def Main():
    anime = pandas.read_csv("anime.csv")
    anime = No_Hentai(anime)
    generes = Get_Diffrent_Generes(anime)
    print()
    y = input("What kind of genere are you looking for? ")
    print()
    while y.lower() != "quit":
        if y.lower() == "all":
            for x in generes:
                count_generes(x,anime)
            y = "quit"
        else:
            count_generes(y.capitalize(),anime)
            print()
            y = input("What other anime generes are you into? ")
            print()


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

#automatically create a list of all anime generes that arn't problimatic.
def Get_Diffrent_Generes(good_list):
    generes = []
    for rows in good_list:
        if rows[2] == "genre":
            pass
        else:
            separate_generes = rows[2].split()
            for x in separate_generes:
                clean_x = x.strip(",")
                for y in generes:
                    if y == clean_x:
                        generes.remove(clean_x)
                generes.append(clean_x)
    return generes

def count_generes(name,good_list):
    count = 0
    for rows in good_list:
        if rows[2] == "genre":
            pass
        else:
            separate_generes = rows[2].split()
            for y in separate_generes:
                clean_y = y.strip(",")
                if clean_y == name:
                    count += 1
    print (f"there are {count} kinds of {name} animes")


Main()