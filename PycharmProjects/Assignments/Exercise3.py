"""Developing in Third Party Framework
    Priya Vora
    5/7/2018
    Table of Contents
"""
loop = False
number_of_chapters = 0
list_of_chapters = {}
class Chapter():
    def __init__(self, title, starting_page):
        self.title = title
        self.starting_page = starting_page

while not loop:
    try:
        number_of_chapters = int(input("\nHow many chapters are in your book?"))
        loop = True
    except ValueError:
        print("\tInvalid input!")


for eachChapter in range(0,number_of_chapters):
    current_title = (input("\nWhat is the title of Chapter " + str(eachChapter+1) + "?")).strip()
    valid = False
    while not valid:
        try:
         page = int(input("\nWhat page does Chapter " + str(eachChapter+1) + " start on?").strip())
         current_starting_page = int(page)
         current_chapter = Chapter(current_title, current_starting_page)
         list_of_chapters[current_title] = current_starting_page
         valid = True
        except ValueError:
            print("\tInvalid Input")

count = 1
print("\nTable of Contents")
for title ,page in list_of_chapters.items():
    chapter_portion = "Chapter " + str(count) + ": "

    titleData =  chapter_portion + title.strip() + " "
    amount = 40 - len(titleData)
    print("Len of the Title Data: " + str(len(titleData)))
    print(titleData.ljust(2), end="", flush=True)
    data = " " + str(page) + " "
    print(data.rjust(amount+1, "*"))


    count = count + 1


