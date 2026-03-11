class Document:
    def display(self):
        return "Отображение документа"


class PdfDocument(Document):
    def display(self):
        return "Отображение PDF документа"


class WordDocument(Document):
    def display(self):
        return "Отображение Word документа"
