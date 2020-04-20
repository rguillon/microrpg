import yaml
from pylatex.basic import NewLine
from pylatex.utils import bold

from .book import Book


class Skill:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def add_to_book(self, book: Book):
        book.append(bold(self.name))
        book.append(" : ")
        book.append(self.desc)
        book.append(NewLine())
        book.append(NewLine())


def skill_constructor(loader, node):
    values = loader.construct_mapping(node, deep=True)

    name = values['name']
    desc = values['desc']

    return Skill(name, desc)


yaml.add_constructor('!skill', skill_constructor)
