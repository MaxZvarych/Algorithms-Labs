import csv
from Film import Film
def read_csv_and_add_to_array(filename):
    list_of_films= []
    with open(filename, 'r') as csv_films:
        reader = csv.reader(csv_films)
        for row in reader:
            list_of_films.append(Film(row[0], int(row[1]), int(row[2])))
        return list_of_films



