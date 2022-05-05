import pandas

def Main():
    anime = pandas.read_csv("anime.csv")
    anime = No_Hentai(anime)
    rows = Top_Animes(anime)
    Find_Anime(rows)

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

def Top_Animes(anime):
    rowlist = []
    tvlist = []
    movielist = []
    for row in anime:
        if row[5] == "Blank":
            pass
        else:
            rowlist.append(f"{row[5]} {row[1]}")
            if row[3] == "TV":
                tvlist.append(f"{row[5]} {row[1]}")
            elif row[3] == "Movie":
                movielist.append(f"{row[5]} {row[1]}")
            else:
                pass
    rowlist.sort(reverse= True)
    tvlist.sort(reverse= True)
    movielist.sort(reverse= True)
    print()
    print("Top Rated Animes!")
    print(f"#1 {rowlist[1]}")
    print(f"#2 {rowlist[2]}")
    print(f"#3 {rowlist[3]}")
    print(f"#4 {rowlist[4]}")
    print(f"#5 {rowlist[5]}")
    print()
    print("Top Rated Anime Movies!")
    print(f"#1 {movielist[1]}")
    print(f"#2 {movielist[2]}")
    print(f"#3 {movielist[3]}")
    print(f"#4 {movielist[4]}")
    print(f"#5 {movielist[5]}")
    print()
    print("Top Rated Anime TV Shows!")
    print(f"#1 {tvlist[1]}")
    print(f"#2 {tvlist[2]}")
    print(f"#3 {tvlist[3]}")
    print(f"#4 {tvlist[4]}")
    print(f"#5 {tvlist[5]}")
    return rowlist

def Find_Anime(rows):
    print()
    search = input("Do you have an anime that you are looking for? (yes or no): ")
    print()
    while search.lower() != "no":
        if search.lower() == "yes":
            anime = input("Search for a title or part of a title: ")
            there = False
            print()
            for row in rows:
                if anime.lower() in row.lower():
                    there = True
                    print(f"{row}")
                    print()
            if there == False:
                print("Nothing here")
                print()
            search = input("wanna keep searching? (yes or no): ")
            print()
        elif search.lower() == "no":
            pass
        else:
            search = input("Please put 'yes' or 'no': ")
            print()

    
Main()