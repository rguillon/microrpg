# coding: utf-8
import os
import yaml

from pylatex import NoEscape
from microrpg.book import Book

import microrpg.effector
import microrpg.skills
import microrpg.item

from microrpg.listfile import ListFile


def build_rules_book():
    book = Book('microRPG', output_dir + "/rules_book")
    book.add_tex_src("text_fr/charrules.tex")
    book.add_tex_src("text_fr/charsheet.tex")
    book.add_tex_src("text_fr/gm_help.tex")
    book.add_tex_src("text_fr/npc_sheet.tex")
    book.to_pdf()


def build_cyberpunk_book():
    skills_file = ListFile("Compétences", "text_fr/cyberpunk/skills.yaml")
    effector_file = ListFile("Equipements", "text_fr/cyberpunk/effectors.yaml")
    microrpg.effector.__singleton__ = effector_file
    weapons_file = ListFile(None, "text_fr/cyberpunk/weapons.yaml")
    tools_file = ListFile(None, "text_fr/cyberpunk/tools.yaml")

    cyberpunk_book = Book('microCyberpunk', "out/cp2020")
    cyberpunk_book.add_tex_src("text_fr/cyberpunk/cyberpunk.tex")
    skills_file.add_to_book(cyberpunk_book)
    effector_file.add_to_book(cyberpunk_book)
    weapons_file.add_to_book(cyberpunk_book)
    tools_file.add_to_book(cyberpunk_book)
    cyberpunk_book.to_pdf()


if __name__ == '__main__':
    output_dir = "out";

    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass

    # build_rules_book()
    build_cyberpunk_book()
