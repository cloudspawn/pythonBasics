class Rectangle:
    def __init__(self, width, height, color="red"):
        self.width = width
        self.height = height
        self.color = color

    def calculate_area(self):
        return self.width * self.height

    def info(self):
        return [self.width, self.height, self.color]


rect1 = Rectangle(10, 20, "bleu")
print(rect1.info(), type(rect1), "surface est de ", rect1.calculate_area())

# class Cake:
#     def __init__(self, flavor):
#         self.flavor: flavor

#     def couper_en_part(self):
#         print("le gateau est coupé en 4 parts!")


"""Definir des calsse d'outils"""


class BoiteAOutil:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        pass

    def remove_tool(self, tool):
        pass


class Tournevis:
    def __init__(self, size):
        self.size: size

    def tighten(self, screw):
        pass

    def loosen(self, screw):
        pass


class Marteau:
    def __init__(self, color="red"):
        self.color = color

    def paint(self, color):
        pass

    def hammer_in(self, nail):
        pass

    def remove(self, nail):
        pass


tourn2 = Tournevis(10)
print(type(tourn2))
