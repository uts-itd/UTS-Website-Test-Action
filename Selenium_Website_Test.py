from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
#from selenium.webdriver.chrome.service import Service
import os
from selenium import webdriver
#import subprocess

# define ze options
fireFox_options = webdriver.FirefoxOptions()
chrome_options = webdriver.ChromeOptions()
edge_options = webdriver.EdgeOptions()
options = Options()

# see no evil
#fireFox_options.add_argument("--headless") # watch your head!
#chrome_options.add_argument("--headless")
#edge_options.add_argument("--headless")

#chrome_options.add_argument("--disable-dev-shm-usage")

# manipulating the dimensions of space..... but not time
fireFox_options.add_argument("--kiosk") # Firefox is not chromium!!! 
#fireFox_options.add_argument("--height=1080") # Firefox is not chromium!!! 
chrome_options.add_argument("--kiosk")
edge_options.add_argument("--kiosk")

# Point me in the right direction baby!
driverFirefox = webdriver.Remote( 
command_executor="http://localhost:4444",
options=fireFox_options
)

# Point me in the right direction baby The sequel!
driverChrome = webdriver.Remote( 
command_executor="http://localhost:4444",
options=chrome_options
)

# Point me in the right direction baby The Threequel! 
driverEdge = webdriver.Remote( 
command_executor="http://localhost:4444",
options=edge_options
)

driverFirefox.get('https://lx.uts.edu.au/') #Fire up the Fox Cannon!
driverChrome.get('https://lx.uts.edu.au/')  #Fire up the Chrome Cannon!
driverEdge.get('https://lx.uts.edu.au/')    #Fire up the Edge Cannon!
 
# Run deez tests!
def webtest(driver):

        action_chain = ActionChains(driver)

        #driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click() home page button
        try:
                #Home page test
                #Nav buttons 
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div/div/ul/li[1]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div/div/ul/li[2]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div/div/ul/li[3]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div/div/ul/li[4]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div/div/ul/li[5]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div/div/ul/li[6]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
                #End Nav buttons

                #Search bar 
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[2]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[2]/div/div/form/input").send_keys('careers')
                driver.find_element(By.CSS_SELECTOR, ".search-form").submit()
                driver.implicitly_wait(20) # If it takes 10 seconds to hit the ground, how high is the building?
                driver.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div[2]/div[1]/div[2]/div/h3/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
                #End of search bar

                #Slick Arrows top
                driver.find_element(By.XPATH,"//main[@id='main']/div/div[2]/section/div/div/div/div/div[2]/div[2]/a").click()
                driver.find_element(By.XPATH,"//img[@alt='UTS-header']").click()
                driver.find_element(By.XPATH,"//main[@id='main']/div/div[2]/section/div/div/button[2]").click()
                driver.find_element(By.XPATH,"//main[@id='main']/div/div[2]/section/div/div/div/div/div[3]/div[2]/a").click()
                driver.find_element(By.XPATH,"//img[@alt='UTS-header']").click()
                driver.find_element(By.XPATH,"//main[@id='main']/div/div[2]/section/div/div/button[2]").click()
                driver.find_element(By.XPATH,"//main[@id='main']/div/div[2]/section/div/div/button[2]").click()
                #driver.find_element(By.XPATH,"//main[@id='main']/div/div[2]/section/div/div/div/div/div[4]/div[2]/a").click() 
                #driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/section[1]/div/div/div/div/div[4]/div[2]/a").click()
                driver.find_element(By.XPATH,"//img[@alt='UTS-header']").click()
                #End of Slick Arrows top

                #Slick arrows bot
                '''driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/section[4]/div/div/div/div/div[2]/div[2]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/section[4]/div/div/button[2]").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/section[4]/div/div/div/div/div[3]/div[2]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/section[4]/div/div/button[2]").click()
                driver.implicitly_wait(3)
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/section[4]/div/div/button[2]").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/section[4]/div/div/div/div/div[4]/div[2]/a").click()
                driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()'''
                #End of Slick arrows bot

                #End of home page test

                #driver.find_element(By.XPATH, "//a[contains(text(),'LX Resources')]").click()
                #driver.find_element(By.XPATH, "//a[contains(text(),'Inclusive and accessible practices')]").click()
                #driver.find_element(By.XPATH, "//div[@id='ld-expand-253085']/div/a/div[2]").click()
                #driver.find_element(By.XPATH, "//div[@id='learndash_post_253085']/div/div[3]/div[3]/a/span").click()
                #driver.find_element(By.XPATH, "//a[contains(text(),'LX.lab')]").click()
                #driver.find_element(By.XPATH, "//a[contains(text(),'LX Blog')]").click()
                #driver.find_element(By.XPATH, "//main[@id='main']/section[4]/div/div[2]/div/div[2]/div/div[3]/a").click()
                #driver.find_element(By.XPATH, "//img[@alt='UTS-header']").click()
                #driver.find_element(By.XPATH, "//main[@id='main']/div/div[2]/section/div/div/button[2]").click()
                #driver.find_element(By.XPATH, "//a[contains(text(),'opener')]").click()
                
                #driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/section[4]/div/div/div/div/div[2]/div[2]/a").click()
                #driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img").click()
        finally:
                driver.quit() #KILL IT! (WITH FIRE)
                print(driver.current_url)

webtest(driverFirefox)
webtest(driverChrome)
webtest(driverEdge)

# R.I.P Joe Rogan
# R.I.P Filthy Frank 
# Do you pick your feet in Poughkeepsie?