# coding: utf-8

from pylatex import Subsection
import yaml

from pylatex import Document, Tabularx, NoEscape
from pylatex.utils import bold
from pylatex.basic import *

from .book import Book

__singleton__ = None


class Effector:
    def __init__(self, name: str, desc: str, cost_effect: float):
        self.name = name
        self.desc = desc
        self.cost_effect = cost_effect

    def __repr__(self):
        return str(self.name + " : " + self.desc + " : " + str(self.cost_effect))

    def add_to_book(self, book: Book):
        book.append(NoEscape("\\noindent\\makebox[\\linewidth]{\\rule{\\columnwidth}{0.4pt}}"))
        book.append(LineBreak())
        book.append(bold(self.name))
        book.append(NoEscape("\\hspace*{\\fill}"))
        book.append(bold("x " + str(self.cost_effect)))
        book.append(LineBreak())
        book.append(self.desc)
        book.append(NewLine())
        book.append(NewLine())

class EffectorList:
    def __init__(self, name, yaml_node):
        self.name = name
        self.items = yaml_node

    def add_to_book(self, book: Book):
        with book.create(Subsection(self.name)):
            for item in self.items:
                item.add_to_book(book)

class EffectorFile:
    def __init__(self, filename):
        yaml_doc = yaml.load(open(filename, mode='r', encoding="utf-8"), Loader=yaml.FullLoader)
        self.itemlists = []
        for yaml_node in yaml_doc:
            print(str(yaml_node))
            try:
                self.itemlists.append(EffectorList(yaml_node, yaml_doc[yaml_node]))
            except TypeError:
                self.itemlists.append(yaml_node)
        global __singleton__
        __singleton__ = self

    def add_to_book(self, book: Book):
        for itemlist in self.itemlists:
            itemlist.add_to_book(book)


def effector_constructor(loader, node):
    values = loader.construct_mapping(node, deep=True)

    return Effector(values['name'], values['desc'], values['effect'])


yaml.add_constructor('!effector', effector_constructor)


def get_effector(name):
    try:
        for item in __singleton__.itemlists:
            if item.name == name:
                return item
        raise KeyError("Effecot %s not found"%name)
    except KeyError as e:
        raise ValueError(e)

