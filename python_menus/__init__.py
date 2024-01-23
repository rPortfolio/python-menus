import os
from colorama import Fore, Style


#Key codes
ENTER = "\x0D"
UP = "\x1b[A"
DOWN = "\x1b[B"
UNDERLINE = "\u0332"



class MenuOption:
    def __init__(self, text:str, func):
        self.text = text
        self.func = func


class Menu:
    def __init__(self, title:str, options=[]):
        self.title = title
        self.options = options
        self.selected_option = 0

  #Displays the menu
    def display(self):
        os.system('clear')
        print(Style.RESET_ALL + UNDERLINE.join(self.title))
        for option in range(len(self.options)):
            if option == self.selected_option:
                print(Fore.BLUE + "   > " + self.options[option].text)
            else:
                print(Style.RESET_ALL + "     " + self.options[option].text)

    #Runs option func
    def confirm(self):
        if self.options[self.selected_option].func:
            self.options[self.selected_option].func()

    #Up and Down selection
    def up(self):
        if self.selected_option == 0:
            self.selected_option = len(self.options)-1
        else:
            self.selected_option -= 1
        self.display()

    def down(self):
        if self.selected_option == len(self.options)-1:
            self.selected_option = 0
        else:
            self.selected_option += 1
        self.display()
  
    #Adds or removes MenuOption. Will rarely be used.
    def add_option(self, text, func):
        new_option = MenuOption(text, func)
        self.options.append(new_option)

    def remove_option(self, index):
        self.options.pop(index)