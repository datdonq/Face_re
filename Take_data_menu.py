
from pathlib import Path
import PySimpleGUI as sg
from take_data import take_data
def take_data_window(settings):
    menu_def = [["Help", ["About", "Exit"]], ["Tools", ["Face Recognition"]]]
    layout = [[sg.Image(key="-IMAGE-")],
              [sg.MenubarCustom(menu_def, tearoff=False)],
              [sg.T("Input Your name:", s=15, justification="r"),
               sg.I(key="-NAME-")  ],
              [sg.Exit(s=16, button_color="tomato"),
               sg.B("Take pictures", s=16)],
              ]
    window_title = settings["GUI"]["title"]
    window = sg.Window(window_title, layout, use_custom_titlebar=True)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "About":
            window.disappear()
            sg.popup(window_title, "Version 1.0", grab_anywhere=True)
            window.reappear()
        if event == "Take pictures":
            take_data(values["-NAME-"])
    window.close()
def take_data_menu():
    SETTINGS_PATH = Path.cwd()
    settings = sg.UserSettings(
        path=SETTINGS_PATH, filename="config.ini", use_config_file=True, convert_bools_and_none=True
    )
    theme = settings["GUI"]["theme"]
    font_family = settings["GUI"]["font_family"]
    font_size = int(settings["GUI"]["font_size"])
    sg.theme(theme)
    sg.set_options(font=(font_family, font_size))
    take_data_window(settings)