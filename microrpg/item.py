import yaml
from pylatex import (NoEscape,  MdFramed)

from pylatex.basic import *
from pylatex.utils import bold

from .book import Book
from .effector import get_effector


class Item:

    def __init__(self, name, desc, effects, effectors):
        self.name = name
        self.desc = desc
        self.effects = effects
        self.effectors = effectors

    def __get_cost(self):
        cost = 0
        for effect in self.effects.values():
            cost += effect * (effect - 1) / 2
        for effector in self.effectors:
            cost = cost * effector.cost_effect
        return int(cost)

    def add_to_book(self, book: Book):

        with book.create(MdFramed()) as box:


            box.append(bold(self.name))
            box.append(NoEscape("\\hspace*{\\fill}"))
            box.append(bold(self.__get_cost()))
            box.append(" ¥€$\n")
            box.append(NoEscape(r"\noindent\rule{\columnwidth}{1pt}"))
            box.append(LineBreak())
            box.append(LineBreak())
            box.append(self.desc)
            box.append(NewLine())




def item_constructor(loader, node):
    values = loader.construct_mapping(node, deep=True)

    name = values['name']
    desc = values['desc']
    effects = {}
    modifiers = []

    for effect in values['effects']:
        for effect_name in effect:
            effects[effect_name] = int(effect[effect_name])

    try:
        for modif_name in values['modifs']:
            modifiers.append(get_effector(modif_name))
    except KeyError:
        # An item may have no modifs
        pass

    return Item(name, desc, effect, modifiers)


yaml.add_constructor('!item', item_constructor)
