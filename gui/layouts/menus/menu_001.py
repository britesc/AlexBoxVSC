import gui.includes.inc_gui_display as gui

# Menu menu_001.py

""" Create and Dislpay Main Menu. """
def display_menu_001(pos: int):
    icons_list = ["/images/n/c/return.565","/images/n/c/system.565", "/images/n/c/config.565"]
    headings_list = ["Return","System", "Config"]
    icons_column = 6
    headingings_column = 50
    column_increment = 28
    list_items = len(headings_list) # example 5
    max_rows = 5
    rows = 0    
    color = display.color(0,0,0)
    gui.display.fill(color)
    gui.display.rect(1,1,318,43,gui.display.color(255,255,0),False)
    gui.display.image(3,3,"/images/s/c/ears.565")
    gui.display.upscaled_text(50,15,"Main",gui.display.color(255,255,0),upscaling=2)
    gui.display.rect(1,48,318,192,gui.display.color(0,0,0),True )
    gui.display.rect(1,48,318,192,gui.display.color(255,255,0),False)
    if pos < 0:
        pos = 0
    if pos > list_items:
        pos = list_items
     
    for index in range(pos, len(icons)):
        row_place1 = 54 + (column_increment * (index - pos))
        gui.display.image(icons_column,row_place1,icons_list[index])
        row_place2 = 62 + (column_increment * (index - pos))
        gui.display.upscaled_text(headingings_column,row_place2, headings_list[index],gui.display.color(255,255,0),upscaling=2)
        rows = rows + 1
        if rows > max_rows:
            break
    
    if backlight.value() == False:
        backlight.on()