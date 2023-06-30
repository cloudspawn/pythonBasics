import csv

# fichier = open("hello.txt", "w")
# fichier.write("Hello world")
# fichier.close()

# fermer automatiquement le fichier avec with
# with open("file.txt") as fichier:
#     for ligne in fichier:
#         print(ligne)

# with open("couleurs_preferees.csv") as fichier_csv:
#     reader = csv.reader(fichier_csv, delimiter=",")
#     for ligne in reader:
#         print(ligne)

# version avec dictreader pour prise en compte entete
with open("couleurs_preferees.csv", mode="r") as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=",")
    for ligne in reader:
        print(
            ligne["nom"]
            + " travaille en tant que "
            + ligne["metier"]
            + " et sa couleur preferee est "
            + ligne["couleur_preferee"]
        )
