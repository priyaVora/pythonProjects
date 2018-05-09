"""Developing in Third Party Framework
    Priya Vora
    5/7/2018
    Table of Contents Enhanced
"""
import sys

class Chapter(object):
    def __init__(self, title, starting_page):
        self.title = title
        self.starting_page = starting_page

class TableContentSetter(object):
    loop = False
    number_of_chapters = 0
    list_of_chapters = {}

    def start(self):
        self.prompt_number_of_chapters()
        self.prompt_title()
    def prompt_number_of_chapters(self):
        while not self.loop:
            try:
                self.number_of_chapters = int(input("\nHow many chapters are in your book?"))
                self.loop = True
            except ValueError:
                sys.stderr.write(" Invalid Input\n")
    def prompt_title(self):
        current_loop = False
        for eachChapter in range(0, self.number_of_chapters):
            while not current_loop:
                current_title = (input("\nWhat is the title of Chapter " + str(eachChapter + 1) + "?")).strip()
                if len(current_title) > 20:
                    sys.stderr.write(" Title is too long\n")
                else:
                    current_loop = True

            valid = False
            self.prompt_for_page(current_title,eachChapter, valid)
            current_loop = False
    def prompt_for_page(self, current_title, eachChapter, valid):
        while not valid:
            try:
                page = int(input("\nWhat page does Chapter " + str(eachChapter + 1) + " start on?").strip())
                current_starting_page = int(page)
                current_chapter = Chapter(current_title, current_starting_page)
                if current_starting_page > 999:
                    sys.stderr.write(" Page number is invalid\n")
                else:
                    self.list_of_chapters[current_title] = current_starting_page
                    valid = True
            except ValueError:
                sys.stderr.write(" Invalid Input\n")

class PrintTableContent(object):
    def __init__(self, list_of_chapters):
        self.count = 1
        self.list_of_chapters = list_of_chapters

    def print_table(self):
        print("\nTable of Contents")
        for title, page in self.list_of_chapters.items():
            chapter_portion = "Chapter " + str(self.count) + ": "

            titleData = chapter_portion + title.strip() + " "
            amount = 40 - len(titleData)
            print(titleData.ljust(2), end="", flush=True)
            data = " " + str(page) + " "
            print(data.rjust(amount + 1, "*"))

            self.count = self.count + 1

table_content = TableContentSetter()
table_content.start()
printTable = PrintTableContent(table_content.list_of_chapters)
printTable.print_table()


