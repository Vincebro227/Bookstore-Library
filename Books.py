
class Books:

    def __init__(self, title, author, description, pages) -> None:
        self.title = title
        self.author = author
        self.description = description
        self.pages = pages

    def __str__(self):
        string = f"The current book you have selected is {self.title}.\n"
        string += f"It is written by {self.author} and contains {self.pages}.\n"
        string += f"Here is a short description {self.description}.\n"
        return string