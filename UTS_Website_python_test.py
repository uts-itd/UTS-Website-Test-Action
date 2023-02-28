
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from selenium import webdriver


chromedriver_autoinstaller.install()


s = Service('/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")


driver = webdriver.Chrome(service=s, options=options)
# navigate to eoi webpage
driver.get('https://project-cad-sandpit.sandpit.itu.uts.edu.au/cad/eoi')

#try:


#finally:
    #driver.quit()
