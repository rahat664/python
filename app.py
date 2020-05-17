import csv
filename = "movie_metadata2.csv"
with open(filename, 'rt', encoding='utf8', newline='') as csv_file:
    csvreader = csv.reader(csv_file)
