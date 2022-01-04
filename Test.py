import PySimpleGUI as sg

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def youtube(website):

    service = Service(executable_path=ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(chrome_options=options, service=service)

    browser.maximize_window()
    browser.get("https://www.youtube.com/")


    search = browser.find_element(By.CLASS_NAME, "ytd-searchbox")
    search.click()

    write = browser.find_element(By.NAME, "search_query")
    write.send_keys(website)
    browser.find_element(By.ID, "search-icon-legacy").click()

    browser.close()

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

print(event, values[0], values[1], values[2])   

if event == "Submit":
    youtube(values[2])    