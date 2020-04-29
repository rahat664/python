import csv
with open('movie_metadata.csv', 'r',encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line['imdb_score'],line['movie_title'],line['director_name'])
