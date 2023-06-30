class Film:
    def __init__(self, name):
        self.name = name

    def watch(self):
        print(f"Bon visionnage de {self.name} !")


class FilmCassette(Film):
    def __init__(self, name):
        """Initialise le nom et la bade magnetique"""
        self.name = name
        self.magnetic_tape = True

    def rewind(self):
        """Rembobine le film"""
        print("Le film est en train d'etre rembobiné !")
        self.magnetic_tape = True


class FilmDvd(Film):
    pass


class FilmBlueray(Film):
    pass


film1 = Film("Starwars")
film_dvd1 = FilmDvd("Leon")
film_blueray1 = FilmBlueray("James Bond")
film_cassette1 = FilmCassette("Blade Runner")

film1.name
film1.watch()

film_cassette1.name
film_cassette1.watch()
film_cassette1.rewind()

film_dvd1.watch()
film_blueray1.watch()
