# "r" - read
# "w" - write
# "ri" - read/write
# "x" - create
# "a" - append

try:
 with open("class-06-files/films.txt", "r+", encoding="utf-8") as list_films:
      print(list_films.read())
      print(list_films.read())
      list_films.write("Piratas do Caribe/n")
except FileNotFoundError:
  print("arquivo não encontrado!")
  
try:
     with open("class-06-files/files/films.txt", "r+", encoding="utf-8") as list_films:
        print(list_films.read())
        print(list_films.read())
        list_films.write("Piratas do Caribe/n")
        list_films.seek(0)
        print(list_films.readlines())

        list_films.seek(0)
        array_films = list_films.readlines()

        for film in array_films:
            print(film.upper)
except FileNotFoundError:
  print("arquivo não encontrado!")


