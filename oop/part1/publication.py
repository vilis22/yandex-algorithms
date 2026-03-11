class Publication:
    def __init__(self, title):
        self.title = title


class Book(Publication):
    def get_author(self, author_name):
        return f"Автор книги '{self.title}' - {author_name}"
