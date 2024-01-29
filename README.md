# python-menus

A simple python menu system for linux terminals.

## How to Use
1. Make a Menu object with a list of MenuOptions
2. Pass a function into the MenuOption
```python
main_menu = Menu("Menu", [
    MenuOption("Menu 2", lambda : switch_menu(menu_2)),
    MenuOption("Side Menu", lambda : switch_menu(side_menu)),
    MenuOption("Unused", None),
    MenuOption("Exit", quit)
])
```

The example shows its use in combination with readkey to allow for the arrow keys to move the menu's cursor.
