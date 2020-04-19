# coding: utf-8
import os
import yaml

from microrpg.book import Book
from microrpg.effector import EffectorFile;
from microrpg.skills import SkillsFile
from microrpg.item import ItemsFile

if __name__ == '__main__':
    output_dir = "out";

    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass

    #book = RulesBook(output_dir+"/rules_book")
    #book.add_tex_src("text_fr/charrules.tex")
    #book.add_tex_src("text_fr/charsheet.tex")
    #book.add_tex_src("text_fr/gm_help.tex")
    #book.add_tex_src("text_fr/npc_sheet.tex")
    #book.to_pdf()


    skills_file = SkillsFile("text_fr/cyberpunk/skills.yaml")
    effector_file = EffectorFile("text_fr/cyberpunk/effectors.yaml")
    weapons_file = ItemsFile("text_fr/cyberpunk/weapons.yaml")


    cyberpunk_book = Book("out/cp2020")
    skills_file.add_to_book(cyberpunk_book)
    effector_file.add_to_book(cyberpunk_book)
    weapons_file.add_to_book(cyberpunk_book)
    cyberpunk_book.to_pdf()
