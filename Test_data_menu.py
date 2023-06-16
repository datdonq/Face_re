
from pathlib import Path
import PySimpleGUI as sg
from take_data import take_data
from test_data import *
from take_test_data import *
def test_data_window(settings):
    file_types = [("JPEG (*.jpg)", "*.jpg"),
                  ("All files (*.*)", "*.*")]
    menu_def = [["Help", ["About", "Exit"]], ["Tools", ["Face Recognition"]]]
    layout = [[sg.Image(key="-IMAGE-")],
              [sg.MenubarCustom(menu_def, tearoff=False)],
              [sg.T("Input Image Test:", s=15, justification="r"),
               sg.I(key="-IM-"),
               sg.FileBrowse(file_types=file_types)],
              [sg.B("Recognition with exist image", s=16)],
              [sg.Exit(s=16, button_color="tomato"),
               sg.B("Recognition by your picture", s=16)],
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
        if event == "Recognition with exist image":
            img=cv2.imread(values["-IM-"])
            return test_data(img)
        if event == "Recognition by your picture":
            img=take_test_data()
            return img
    window.close()
def test_data_menu():
    SETTINGS_PATH = Path.cwd()
    settings = sg.UserSettings(
        path=SETTINGS_PATH, filename="config2.ini", use_config_file=True, convert_bools_and_none=True
    )
    theme = settings["GUI"]["theme"]
    font_family = settings["GUI"]["font_family"]
    font_size = int(settings["GUI"]["font_size"])
    sg.theme(theme)
    sg.set_options(font=(font_family, font_size))
    img=test_data_window(settings)
    return img
# test_data_menu()