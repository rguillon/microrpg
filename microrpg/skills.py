from .book import Book

from pylatex import Subsection
from pylatex.utils import bold
from pylatex.basic import *
import yaml


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


class SkillsList:
    def __init__(self, name, yaml_node):
        self.name = name
        self.items = yaml_node

    def add_to_book(self, book: Book):
        with book.create(Subsection(self.name)):
            for item in self.items:
                item.add_to_book(book)

class SkillsFile:
    def __init__(self, filename):
        yaml_doc = yaml.load(open(filename, mode='r', encoding="utf-8"), Loader=yaml.FullLoader)
        self.itemlists = []
        for list_name in yaml_doc:
            self.itemlists.append(SkillsList(list_name, yaml_doc[list_name]))
    def add_to_book(self, book: Book):
        for itemlist in self.itemlists:
            itemlist.add_to_book(book)

def skill_constructor(loader, node):
    values = loader.construct_mapping(node, deep=True)

    name = values['name']
    desc = values['desc']

    return Skill(name, desc)


yaml.add_constructor('!skill', skill_constructor)

