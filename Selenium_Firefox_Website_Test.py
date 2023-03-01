from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service





s = Service('/usr/local/bin/geckodriver')
options = webdriver.FirefoxOptions()
options = Options()
#options.add_argument("--ignore-certificate-errors")
options.add_argument("--private")
#options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")


driver = webdriver.Firefox(service=s, options=options)
# navigate to eoi webpage
driver.get('https://www.uts.edu.au/')
