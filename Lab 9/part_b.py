#Part B

#1
class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return f"Document title: {self.title}"

#2
class PDFDocument(Document):
    def __init__(self, title):
        super().__init__(title)

    #3
    def describe(self):
        return f"PDF title: {self.title}"

class TextDocument(Document):
    def __init__(self, title):
        super().__init__(title)

    #3
    def describe(self):
        return f"Text title: {self.title}"

#4
documents = [
    PDFDocument("Tokyo Disaster Prevention"),
    TextDocument("Notes from 9/24-26"),
    PDFDocument("Loneliness Epidemic"),
    TextDocument("JP Practice P.91"),
]

#5
for document in documents:
    print(document.title)