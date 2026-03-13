class Chapter:
    def __init__(self, title: str) -> None:
        self.title = title

    def get_title(self) -> str:
        return self.title


class Book:
    def __init__(self, title: str, chapters: list[str]) -> None:
        self.title = title
        self.chapters = [Chapter(chapter) for chapter in chapters]

    def get_table_of_contents(self) -> str:
        contents = [self.title] + [
            f"Глава {i}: {chapter.get_title()}" for i, chapter in enumerate(self.chapters, start=1)
        ]
        return "\n".join(contents)
