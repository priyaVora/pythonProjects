"""Developing in Third Party Framework
    Priya Vora
    5/7/2018
    Word Game
"""

""" Create a loop in which two players are continuously prompted to supply a word, starting with Player 1. Ensure that there is a way to exit the loop, such as by typing "0"."""
import sys


def generate_last_two_chars(previous_word):
    last_chars = previous_word[(len(previous_word) - 2):len(previous_word)]
    return last_chars

class wordGame(object):
    words_used = []
    def __init__(self,  player_one, player_two):
        self.player_one  = player_one
        self.player_two = player_two



    def add_word(currentWord):
            print("Add:  " + str(currentWord))


    def prompt_user(self):
        not_loop = False
        count = 0
        while not not_loop:
            if count % 2 ==0:
                player_one_input = input(player_one.name + ": Please enter your word.")
                if player_one_input == str(0):
                    break
                elif len(player_one_input) < 3:
                    sys.stderr.write('\n\nWord is too short!\n')
                    not_loop = False
                elif self.words_used.__contains__(player_one_input.lower()):
                    sys.stderr.write("\n\nWhoops! Can't repeat words!\n")
                    not_loop = False
                else:
                    validCheck = True
                    lastTwo = generate_last_two_chars(player_one_input)
                    check = "" + player_one_input[0] + player_one_input[1]
                    print("Check: " + str(check))
                    if lastTwo == check:
                        validCheck = True
                    else:
                        if count != 0:
                            validCheck = False
                            not_loop = False
                            sys.stderr.write("\n\nStart of the word doesn't match previous word.Try Again!\n")
                        if validCheck == True:
                            count = count + 1
                            print("Count: " + str(count))
                            print("Word: " + player_one_input)
                            self.words_used.append(player_one_input.lower())
                            print("Next Valid last two chars: " + str(lastTwo))
            else:
                player_two_input = input(player_two.name + ": Please enter your word.")
                if player_two_input == str(0):
                    break
                elif len(player_two_input) < 3:
                    sys.stderr.write('\n\nWord is too short!\n')
                    not_loop = False
                elif self.words_used.__contains__(player_two_input.lower()):
                    sys.stderr.write("\n\nWhoops! Can't repeat words!\n")
                    not_loop = False
                else:
                    validCheck = True
                    lastTwo = generate_last_two_chars(player_two_input)
                    check = "" + player_two_input[0] + player_two_input[1]
                    print("Check: " + str(check))
                    print("Last Two: " + lastTwo)
                    if lastTwo == check:
                        validCheck = True
                    else:
                        validCheck = False
                        not_loop = False
                        sys.stderr.write("\n\nStart of the word doesn't match previous word.Try Again!\n")

                    if validCheck == True:
                        count = count + 1
                        print("Count: " + str(count))
                        print("Word: " + player_two_input)
                        self.words_used.append(player_two_input.lower())
                        print("Next Valid last two chars: " + str(lastTwo))




class Player(object):
    def __init__(self, name):
        self.name = name


player_one = Player("Priya")

player_two = Player("Ankita")
word_game = wordGame(player_one, player_two)
word_game.prompt_user()


