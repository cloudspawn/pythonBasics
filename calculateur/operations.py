def sum(a, b):
    return a + b


def substraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Erreur : division par zéro")
