from pylatex import Section, Subsection, Subsubsection
import yaml

from pylatex import Document, Tabularx, NoEscape
from pylatex.utils import bold
from pylatex.basic import *

from .book import Book


class SubList:
    def __init__(self, depth,  name, items):
        self.depth = depth
        self.name = name
        self.items = {}
        for item in items:
            try:
                self.items[item.name] = item
            except AttributeError:
                self.items[item] = SubList(depth + 1, item, items[item])

    def __get_sub_section_for_depth(self):
        if self.depth == 0:
            return Section(self.name)
        elif  self.depth == 1:
            return Subsection(self.name)
        elif  self.depth == 21:
            return Subsection(self.name)

    def add_to_book(self, book: Book):
        if self.name is not None:
            with book.create(self.__get_sub_section_for_depth()):
                for item in self.items:
                    try:
                        self.items[item].add_to_book(book)
                    except TypeError:
                        item.add_to_book(book)
        else:
            for item in self.items:
                try:
                    self.items[item].add_to_book(book)
                except TypeError:
                    item.add_to_book(book)

    def find_item(self, name):
        for item in self.items:
            if item == name:
                return self.items[item]
            else:
                try:
                    if item.name == name:
                        return item
                except AttributeError:
                    try:
                        return self.items[item].find_item(name)
                    except AttributeError:
                        pass

        raise KeyError("Item %s not found")


class ListFile(SubList):
    def __init__(self, name, filename):
        yaml_doc = yaml.load(open(filename, mode='r', encoding="utf-8"), Loader=yaml.FullLoader)
        super().__init__(0, name, yaml_doc)



