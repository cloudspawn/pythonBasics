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


from operations import *


def print_welcome_message():
    print("Bienvenue sur la mini-calculatrice !")


def input_two_number():
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    return num1, num2


def print_menu_and_get_choice():
    print("=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    user_choice = input("Entrez votre choix (1-4) : ")

    while user_choice not in ["1", "2", "3", "4"]:
        user_choice = input("Choix invalide. Entrez votre choix (1-4) : ")

    return user_choice


def run_calculation(user_choice):
    num1, num2 = input_two_number()
    match user_choice:
        case "1":
            result = sum(num1, num2)
        case "2":
            result = substraction(num1, num2)
        case "3":
            result = multiplication(num1, num2)
        case "4":
            result = division(num1, num2)
        case _:
            print("Choix invalide.")
    return result


if __name__ == "__main__":
    print_welcome_message()
    user_choice = print_menu_and_get_choice()
    result = run_calculation(user_choice)
    print(result)
