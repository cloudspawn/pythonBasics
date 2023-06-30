class Rectangle:
    def __init__(self, width, height, color="red"):
        self.width = width
        self.height = height
        self.color = color

    def calculate_area(self):
        return self.width * self.height

    def info(self):
        return [self.width, self.height, self.color, self.calculate_area()]


rect1 = Rectangle(10, 20, "bleu")
rect2 = Rectangle(5, 2)
print(rect1.info(), type(rect1))
print(rect2.info(), type(rect2))

rect2.color = "vert"
print(rect2.info(), type(rect2))

"""Le gateau"""


class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

    def couper_en_part(self):
        print(f"le gateau {self.flavor} est coupé en 4 parts!")

    def change_flavor(self, new_flavor):
        self.flavor = new_flavor


cake1 = Cake("chocolate")
cake1.couper_en_part()
cake1.flavor = "banane"
cake1.couper_en_part()
cake1.change_flavor("menthe")
cake1.couper_en_part()


"""Diference entre attribut instance class et statique"""


class Bird:
    """Un oiseau,"""

    def __init__(self):
        """Les attributs definis ici sont des attributs d'instance"""
        self.wings = 2

    def fly(self):
        """Cette methode est une methode d'instance"""
        print("Je vole !")


bird1 = Bird()
bird1.wings
bird1.fly()


class Bird:
    # ici on utilise deux attributs de classe
    names = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions = {}

    def __init__(self, name):
        """les attributs definis ici sont des attributs d'instance"""
        self.position = 1, 2
        self.name = name

        # on accede a l'attribut de classe "positions" avec self
        self.positions[self.position] = self.name

    @classmethod
    def find_bird(cls, position):
        """Retrouve un oiseau selon la position donnée"""
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]} !"

        return "On a rien trouvé ..."


# On peut acceder au variables de classe sans instanciation.
Bird.names
Bird.positions
print(Bird.find_bird((2, 5)))

# On instancie un oiseau
bird2 = Bird("moineau")

# on le retrouve avec la methode find_bird
print(Bird.find_bird((1, 2)))


"""method statique"""


class Bird:
    @staticmethod
    def get_definition():
        return "Animal a sang chaud etc...."


print(Bird.get_definition())


"""Definir des calsse d'outils"""


class BoiteAOutil:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)

    def remove_tool(self, tool):
        index = self.tools.index(tool)
        del self.tools[index]

    def __str__(self):
        return f"Il y'a les outils suivante dans la boite : {self.tools}"


class Tournevis:
    def __init__(self, size):
        self.size = size

    def tighten(self, screw):
        screw.tighten()

    def loosen(self, screw):
        screw.loosen()

    def __repr__(self):
        return f"Tournevis de taille {self.size}"


class Marteau:
    def __init__(self, color="red"):
        self.color = color

    def paint(self, color):
        self.color = color

    def hammer_in(self, nail):
        nail.nail_in()

    def remove(self, nail):
        nail.remove()

    def __repr__(self):
        """representation de l'objet"""
        return f"Marteau de couleur {self.color}"


class Screw:
    MAX_TIGHTNESS = 5

    def __init__(self):
        """initialise son degré de serrage"""
        self.tightness = 0

    def loosen(self):
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        if self.tighten < self.MAX_TIGHTNESS:
            self.tighten += 1

    def __str__(self):
        """retourne une forme lisible de l'objet"""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    def __init__(self):
        """initialise son status dans le mur"""
        self.in_wall = False

    def nail_in(self):
        """Enfonce le clou dans le mur"""
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        """retourne une forme lisible de l'objet"""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}"


tourn2 = Tournevis(10)
print(type(tourn2))

nail1 = Nail()
nail1.nail_in()
print(nail1.__str__())

boite1 = BoiteAOutil()
marteau1 = Marteau("violet")
print(marteau1.__repr__())

print(boite1.__str__())
boite1.add_tool(marteau1)
boite1.add_tool(tourn2)
print(boite1.__str__())
