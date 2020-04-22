import yaml
import itertools
from pylatex import *
from pylatex.basic import *
from pylatex.utils import bold, italic

from .book import Book
from .effector import get_effector


class ColumnBreak(NewPage):
    """A command that adds a line break to the document."""


def get_effect_str(effect: int):
    if effect >= 0:
        return "+" + str(effect)
    else:
        return str(effect)


class Item:

    def __init__(self, name, desc, effects, permanent_effects, effectors):
        self.name = name
        self.desc = desc
        self.effects = effects
        self.permanent_effects = permanent_effects
        self.effectors = effectors

    def __get_cost(self):
        cost = 0
        for effect in self.effects.values():
            cost += effect * (effect - 1) / 2
        for permanent_effect in self.permanent_effects.values():
            cost += 6 * (permanent_effect * (permanent_effect - 1) / 2)
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
            box.append(NoEscape(self.desc))
            box.append(LineBreak())
            box.append(LineBreak())
            with box.create(Tabularx("X|l|r")) as tab:
                for effect, perma_effect, effector in itertools.zip_longest(self.effects, self.permanent_effects, self.effectors):
                    row = []

                    if effect is not None:
                        row.append(effect + ":" + get_effect_str(self.effects[effect]))
                    else:
                        row.append("")

                    if perma_effect is not None:
                        row.append(perma_effect + ":" + get_effect_str(self.permanent_effects[perma_effect]))
                    else:
                        row.append("")

                    if effector is not None:
                        row.append(italic(effector.name))
                    else:
                        row.append("")

                    tab.add_row(row)


def item_constructor(loader, node):
    values = loader.construct_mapping(node, deep=True)

    name = values['name']
    desc = values['desc']
    effects = {}
    permanent_effects = {}
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
    try:
        for permanent_effect in values['permanent_effects']:
            for effect_name in permanent_effect:
                permanent_effects[effect_name] = int(permanent_effect[effect_name])
    except KeyError:
        # An item may have no permanent effects
        pass

    return Item(name, desc, effects, permanent_effects, modifiers)


yaml.add_constructor('!item', item_constructor)
