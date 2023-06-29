# ma_liste = []

# ma_liste = ["a", "z", "b"]
# ma_liste.append("d")
# print(ma_liste)
# ma_liste.remove("b")
# ma_liste.reverse()
# print(ma_liste)
# if "z" in ma_liste:
#     print("est dedans")

# dico_1 = {"chef": "alain", "age": 40, "loisirs": ["foot", "basket", "python"]}
# dico_1["taille"] = 192
# del dico_1["age"]
# print(dico_1)
# print(dico_1["chef"])
# print(dico_1["loisirs"][1])
# print(dico_1["loisirs"][1])

# print(dico_1.keys())

# fruit = input("choisi un fruit :")
# match fruit:
#     case "pomme":
#         print("j'aime les pommes")
#     case "orange":
#         print("j'aime les oranges")
#     case "cerise":
#         print("j'aime pas les cerises")
#     case "banane":
#         print("j'aime pas les bananes")
#     case _:
#         print("je ne connais pas ca")

# for lettre in ma_liste:
#     print(lettre)

# for x in range(4, 10, 2):
#     print(x)


# def capacite(a, b):
#     capa = a
#     while capa > b:
#         capa -= 1
#     return capa, a, b


# print(capacite(10, 5))


# def somme(a, b):
#     """
#     Cette fonction calcule la somme de deux nombres et retourne le résultat.

#     Parameters:
#     a (int): le premier nombre
#     b (int): le deuxième nombre

#     Returns:
#     int: la somme de a et b
#     """
#     return a + b


# nb1 = int(input("premier nombre a additionner :"))
# nb2 = int(input("deuxieme nombre a additionner :"))
# print(somme(nb1, nb2))


# print("Calculateur de salaire horaire")

# salaireM = int(input("votre salaire mensuel : "))
# heureS = int(input("Nombre d'heure travaillées par semaine : "))


# def salaire_horaire(salaire_mensuel, heure_travail_semaine):
#     return salaire_mensuel / (heure_travail_semaine * 4)


# print(salaire_horaire(salaireM, heureS))

# premiere_campagne = {
#     "visiteurs": 10,
#     "conversions": 5,
# }
# deuxieme_campagne = {
#     "visiteurs": 20,
#     "conversions": 5,
# }
# troisieme_campagne = {
#     "visiteurs": 30,
#     "conversions": 8,
# }


# def calculer_taux_de_conversion(campagne):
#     return campagne["visiteurs"] / campagne["conversions"]


# print(calculer_taux_de_conversion(deuxieme_campagne))


# while True:
#     try:
#         x = int(input("Entrer un nombre entier : "))
#         break
#     except ValueError:
#         print("OOps! ce n'est pas un nombre entier, essayez encore... ")

# while True:
#     try:
#         num = input("entrer un numerateur : ")
#         deno = input("entrer un denominateur : ")
#         resultat = int(num) / int(deno)
#         print(f"le resultat est {resultat}")
#         break
#     except ZeroDivisionError:
#         print("Erreur, division par zero !")
#     except ValueError:
#         print("Erreur: conversion de type incorrecte")
