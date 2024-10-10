import gui.includes.inc_gui_display as gui

# Menu menu_101.py

""" Create and Dislpay System Menu. """
def display_menu_101(pos: int):
    icons_list = ["/images/n/c/return.565","/images/n/c/cpu_temp.565","/images/n/c/power.565","/images/n/c/info.565"]
    headings_list = ["Return","System Temp","Battery Status","Information"]
    icons_column = 6
    headingings_column = 50
    column_increment = 28
    list_items = len(headings_list) # example 5
    max_rows = 5
    gui.display_boxes(255, 255, 0, "c", "System", "system.565")
    rows = 0     

    if pos < 0:
        pos = 0
    if pos > list_items:
        pos = list_items
     
    for index in range(pos, len(icons_list)):
        row_place1 = 54 + (column_increment * (index - pos))
        gui.display.image(icons_column,row_place1,icons_list[index])
        row_place2 = 62 + (column_increment * (index - pos))
        gui.display.upscaled_text(headingings_column,row_place2, headings_list[index],gui.display.color(255,255,0),upscaling=2)
        rows = rows + 1
        if rows > max_rows:
            break

    if gui.backlight.value() == False:
        gui.backlight.on()
    