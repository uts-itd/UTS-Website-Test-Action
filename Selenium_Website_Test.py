from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
#from selenium import webdriver
#import subprocess


fireFox_options = webdriver.FirefoxOptions()
chrome_options = webdriver.ChromeOptions()
edge_options = webdriver.EdgeOptions()
options = Options()
#fireFox_options.add_argument("--headless")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
fireFox_options.add_argument("--width=1920")
fireFox_options.add_argument("--height=1080")
edge_options.add_argument("--window-size=1920,1080")
#edge_options.add_argument("--headless")
#options.add_argument("--incognito")

driver1 = webdriver.Remote( 
command_executor="http://192.168.0.2:4444",
options=fireFox_options
)

driver2 = webdriver.Remote( 
command_executor="http://192.168.0.2:4444",
options=chrome_options
)

driver3 = webdriver.Remote( 
command_executor="http://192.168.0.2:4444",
options=edge_options
)

driver1.get('https://lx.uts.edu.au/')
driver2.get('https://lx.uts.edu.au/')
driver3.get('https://lx.uts.edu.au/')

def webtest(driver):
        driver.find_element(By.XPATH, "//a[contains(text(),'LX Resources')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Inclusive and accessible practices')]").click()
        driver.find_element(By.XPATH, "//div[@id='ld-expand-253085']/div/a/div[2]").click()
        driver.find_element(By.XPATH, "//div[@id='learndash_post_253085']/div/div[3]/div[3]/a/span").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'LX.lab')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'LX Blog')]").click()
        driver.find_element(By.XPATH, "//main[@id='main']/section[4]/div/div[2]/div/div[2]/div/div[3]/a").click()
        driver.find_element(By.XPATH, "//img[@alt='UTS-header']").click()
        driver.find_element(By.XPATH, "//main[@id='main']/div/div[2]/section/div/div/button[2]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'opener')]").click()
        driver.find_element(By.ID, "s").click()
        driver.find_element(By.ID, "s").send_keys('careers')
        driver.find_element(By.CSS_SELECTOR, ".search-form").submit()
        driver.implicitly_wait(10) # seconds
        driver.find_element(By.XPATH, "//a[contains(text(),'Tools for threading WIL into your whole of course design: Careers Canvas modules and the TRACK-Learner tool | 12 October')]").click()
        driver.quit()
webtest(driver1)
webtest(driver2)
webtest(driver3)
