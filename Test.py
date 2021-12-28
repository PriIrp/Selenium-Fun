from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# # Use the `install()` method to set `executabe_path` in a new `Service` instance:
service = Service(executable_path=ChromeDriverManager().install())

# # Pass in the `Service` instance with the `service` keyword: 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=service)
browser.maximize_window()
browser.get("https://www.youtube.com/")


#wait = WebDriverWait(browser, 3)
#visible = EC.visibility_of_element_located

search = browser.find_element(By.CLASS_NAME, "ytd-searchbox")
search.click()

write = browser.find_element(By.NAME, "search_query")
write.send_keys("ThinkOrSwim")
browser.find_element(By.ID, "search-icon-legacy").click()
