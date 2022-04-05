import PySimpleGUI as sg

smileys = ["happy", [":)", "xD", ":D", "<3"], "sad", [":(", "T_T"], "other", [":3"]]
smileys_events = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ["File", ["Open", "Save", "---", "Exit"]],
    ["Tools", ["Word Count"]],
    ["Add", smileys],
]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("Untitled", key="-DOCNAME-")],
    [sg.Multiline()],
]

window = sg.Window("Title", layout, size=(300, 300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Word Count":
        print("test")

window.close()
