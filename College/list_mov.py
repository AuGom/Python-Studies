movies = ["exterminador", "rambo", "star wars", "tropa de elite"]
print(movies[1])
print(len(movies))
movies.append("caçadores da arca perdida")
print(movies)
movies.pop()
print(movies)
movies.extend(["poderoso chefao", "magico de oz", "tubarao"])
print(movies)
movies.remove("rambo")
print(movies)
movies.insert(0, "rambo")
print(movies)
for i in movies:
    print(i)
for i in range(len(movies)):
    print(i)
cont = 0
while cont < len(movies):
    print(movies[cont])
    cont += 1
print("\n")
movies2 = ["exterminador", 1985, "arnold", ["rambo", 1982, "stallone", [
    "star wars", 1977, "mark hamill", ["tropa de elite", 2007, "wagner moura"]]]]
for i in movies2:
    print(i)
print("\n")
for i in movies2:
    if isinstance(i, list):
        for z in i:
            print(z)
    else:
        print(i)
print("\n")
