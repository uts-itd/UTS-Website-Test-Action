from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import os
from selenium import webdriver



s = Service('/usr/local/bin/geckodriver')
options = webdriver.FirefoxOptions()
options = Options()
options.add_argument("--private")
options.add_argument("--window-size=1920,1080")



driver = webdriver.Firefox(service=s, options=options)

driver.get('https://www.uts.edu.au/')


try:
    next_button = driver.find_element(By.ID, "node/4087").click()

finally:
    driver.quit()





    #Help me