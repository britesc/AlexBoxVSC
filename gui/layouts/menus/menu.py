"""
    Menu Driver.
"""
# Declare Builtins Imports
import ujson
import gc

# Declare 3rd Party Imports
from lib import utilities_filesystem as fs
import gui.includes.inc_gui_display as gui

""" Create and Dislpay System Menu. """
def display_menu(menu: str, r: int, g: int, b: int, tint: str, pos: int):
    gc.enable()
    icons_column = 6
    headingings_column = 50
    column_increment = 28
    max_rows = 5
    rows = 0    
    if fs.dir_exists("/json"):
        """ Check if file exists! """
        if fs.file_exists("/json/menus.json"):
            with open("/json/menus.json", "rt") as fp:
                menudata = ujson.load(fp)
                
    the_list = menudata['menu'][menu]

    menu_title = menudata['menu'][menu]['heading']
    menu_icon = menudata['menu'][menu]['icon']

    icons_list_t = menudata['menu'][menu]['icons_list']
    icons_list_t = icons_list_t.replace("'","")
    icons_list_t = icons_list_t.replace(" ","")    
    icons_list_t = icons_list_t.replace("{","")
    icons_list_t = icons_list_t.replace("}","")
    icons_list = icons_list_t.split(",")

    headings_list_t = menudata['menu'][menu]['headings_list']
    headings_list_t = headings_list_t.replace("'","")
    headings_list_t = headings_list_t.replace("{","")
    headings_list_t = headings_list_t.replace("}","")
    headings_list = headings_list_t.split(",")    
    
    list_items = len(headings_list) # example 5

    length = sum([1 for _ in headings_list])
    gui.display_boxes(r, g, b, tint, menu_title, menu_icon)
    
    if pos < 0:
        pos = 0
    if pos > list_items:
        pos = list_items
 
    for index in range(pos, len(icons_list)):
        row_place1 = 54 + (column_increment * (index - pos))
        menu_icon_to_show = f"/images/n/{tint}/{icons_list[index]}"
        menu_row_to_show  = headings_list[index].strip()

        gui.display.image(icons_column,row_place1, menu_icon_to_show)
        row_place2 = 62 + (column_increment * (index - pos))
        gui.display.upscaled_text(headingings_column,row_place2, menu_row_to_show,gui.display.color(255,255,0),upscaling=2)

        rows = rows + 1
        if rows > max_rows:
            break    
    gc.collect()
    if gui.backlight.value() == False:
        gui.backlight.on()

if __name__ == "__main__":
    display_menu("103",255,255,0,"c",0)     
                