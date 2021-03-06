# coding: utf-8

import yaml
from pylatex import NoEscape
from pylatex.basic import *
from pylatex.utils import bold

from .book import Book

__effectors__ = {}


class Effector:
    def __init__(self, name: str, desc: str, cost_effect: float):
        self.name = name
        self.desc = desc
        self.cost_effect = cost_effect

        global __effectors__
        __effectors__[name] = self

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


def effector_constructor(loader, node):
    values = loader.construct_mapping(node, deep=True)
    return Effector(values['name'], values['desc'], values['effect'])


yaml.add_constructor('!effector', effector_constructor)


def get_effector(name):
    try:
        return __effectors__[name]
    except AttributeError as e:
        raise ValueError(e)
