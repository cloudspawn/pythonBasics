"""Classes
File - Image
User - Moderator
Post - FilePost
Thread
"""


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        print(f"Fichier '{self.name}'.")


class Image(File):
    pass


class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.passowrd = password

    def login(self):
        pass

    def post(self, thread, content):
        pass

    def make_thread(title, content):
        pass


class Moderator(User):
    def edit(self, post, content):
        pass

    def delete(self, thread, post):
        pass


class Post:
    def __init__(self, user, time_posted, content) -> None:
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        pass


class FilePost(Post):
    def __init__(self, user, time_posted, content, file) -> None:
        super().__init__(user, time_posted, content)
        self.file = file

    def __str__(self) -> str:
        return f"voici la liste des trucs {self.user} {self.time_posted} {self.content} {self.file}"


class Thread:
    def __init__(self, title) -> None:
        self.tilte = title


fileP1 = FilePost("alain", "lundi", "aujourdhui il fait beau et blabla", "toto.tot")
print(fileP1)
