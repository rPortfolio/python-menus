from readchar import readkey #Allows you to get key input
from python_menus import Menu, MenuOption, ENTER, UP, DOWN

current_menu = None
menu_history = [] #Stores the order of every menu you've opened

#Functions that load menus
def set_menu(menu:Menu):
  global current_menu
  current_menu = menu
  current_menu.selected_option = 0 #Resets selection
  current_menu.display()

def switch_menu(menu:Menu):
  set_menu(menu)
  menu_history.append(menu)

#Removes current menu and loads previous menu
def back_menu():
  menu_history.pop(len(menu_history)-1)
  set_menu(menu_history[len(menu_history)-1])

#Menu objects
menu_3 = Menu("Menu 3",[
  MenuOption("Go Back", lambda : back_menu())
])

menu_2 = Menu("Menu 2", [
  MenuOption("Menu 3", lambda : switch_menu(menu_3)),
  MenuOption("Input Test", lambda : input("Input: ")),
  MenuOption("Go Back", lambda : back_menu())
])
#Side menu exists to show that you can get to the same menu from different other menus
side_menu = Menu("Side Menu", [
  MenuOption("Menu 2", lambda : switch_menu(menu_2)),
  MenuOption("Go Back", lambda : back_menu())
])

main_menu = Menu("Menu", [
  MenuOption("Menu 2", lambda : switch_menu(menu_2)),
  MenuOption("Side Menu", lambda : switch_menu(side_menu)),
  MenuOption("Unused", None),
  MenuOption("Exit", quit)
])


#Initializes first menu
switch_menu(main_menu)
print("(Use arrow keys to navigate)")
#Main program loop
running = True
while running:
  #Reacts to key input
  key = readkey()
  if key == UP:
    current_menu.up()
  if key == DOWN:
    current_menu.down()
  if key == ENTER:
    current_menu.confirm()