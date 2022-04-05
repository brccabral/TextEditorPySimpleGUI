import PySimpleGUI as sg


layout = [[]]

window = sg.Window("Title", layout, size=(300, 300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
