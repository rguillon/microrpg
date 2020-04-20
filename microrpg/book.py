import io

from pylatex import Document, Command, NoEscape


class Book(Document):

    def __init__(self, title: str, filename: str):
        document_margin = "20mm"

        geometry_options = {"left": document_margin,
                            "top": document_margin,
                            "right": document_margin,
                            "bottom": document_margin}
        super().__init__('article', inputenc='utf8', geometry_options=geometry_options)
        self.preamble.append(Command('title', title))
        self.preamble.append(Command('author', 'Renaud Guillon'))

        self.preamble.append(Command('date', ''))
        self.preamble.append(Command('usepackage', 'tabularx'))
        self.preamble.append(Command('usepackage', 'multicol'))
        self.preamble.append(Command('usepackage', 'siunitx'))
        self.preamble.append(Command('usepackage', 'pdflscape'))
        self.preamble.append(Command('usepackage[french]', 'babel'))
       # self.preamble.append(Command('usepackage[table]', 'xcolor'))

        self.filename = filename

    def add_tex_src(self, filename: str):
        with io.open(filename, 'r', encoding='utf8') as file:
            content = file.read()
            self.append(NoEscape(content))

    def to_tex(self):
        self.generate_tex(self.filename)

    def to_pdf(self):
        self.generate_pdf(self.filename, clean_tex=False)
