import definition as d
import PySimpleGUI as sg


# website = input("What would you like to search on Youtube? ")
# d.youtube(website=website)

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout, margins=(300,200))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
