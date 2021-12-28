import definition as d
import PySimpleGUI as sg


# website = input("What would you like to search on Youtube? ")
# d.youtube(website=website)

layout = [
    [sg.Text('Please enter your Name, Age, Phone')],
    [sg.Text('Name', size =(15, 1)), sg.InputText()],
    [sg.Text('Age', size =(15, 1)), sg.InputText()],
    [sg.Text('Youtube Search', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
  
window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()
  
# The input data looks like a simple list 
# when automatic numbered
print(event, values[0], values[1], values[2])   

if event == "Submit":
    d.youtube(values[2])    