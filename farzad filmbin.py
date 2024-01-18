number_of_films = int(input())
list_films = []
for i in range(number_of_films):
    list_films.append(input())
for i in list_films:
    print(i.title())