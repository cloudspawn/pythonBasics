import csv

with open("data.csv", mode="r") as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=",")
    for ligne in reader:
        print(ligne)
        print(ligne["nom"] + " travaille en tant que " + ligne["metier"])
