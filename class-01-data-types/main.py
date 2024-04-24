# Primitive Types

milk = "leite desnatado"
volume = 2.5

print(type(milk))
print(type(volume))

preparation1 = volume + 1
preparation2 = milk + "10"

print(preparation1)
print(preparation2)

life_cat = str (volume + 5)

print("o gato bebe" + milk)
print("E tem" + life_cat + "vidas")

print(F"o gato bebe {milk} e tem {life_cat} vidas")
print(F"o gato bebe {milk} e tem {life_cat} vidas")

name = "Davi"
age = 31
is_admin = False #boolean True of False

print(is_admin)
print(type(is_admin))

# Structural Types (Collection)

animes = ["Dragon Ball", "Naruto", "Cavalheiros do Zodiaco", "Death Note"]
          # => 0                1              2                      3
          # <= -4              -3             -2                     -1

print(animes)
print(type(animes))
print(animes[0])
print(animes[3])
print(animes[-1])

list = ["A", 123, True, ["B", "C"]]

print(list[0])
print(list[3])
print(list[-1])
print(list[-1][1])

list[2] = False
list[-1][0] = "0"
print(list)
print(len(list)) # length

# Tuple
tuple = ("A", 123, True)
print(type(tuple))
print(tuple[1])

tuple[1] = 798 # error: tuple is immutable 

print(tuple)

# dict

dict = {
    "name": "Jonatan",
    "age": 19,
    "is_admin": True
}

print(dict)
print(type(dict))

print(dict["name"])
print(dict["age"])
print(dict["is_admin"])