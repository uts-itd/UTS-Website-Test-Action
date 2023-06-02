'''This script stores all the common functions between the 3 test files. Including setup the drivers and the tests itself'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


# see no evil
#firefox_options.add_argument("--headless") # watch your head!
#chrome_options.add_argument("--headless")
#edge_options.add_argument("--headless")

#chrome_options.add_argument("--disable-dev-shm-usage")
def set_options(driver_options):
        # manipulating the dimensions of space..... but not time
        #driver_options.add_argument("--kiosk") # Firefox is not chromium!!! 
        driver_options.add_argument("--start-maximized") #It makes everything work on Chrome and Edge

def setup_driver(driver_options):
# Point me in the right direction baby!
        driver = webdriver.Remote( 
        command_executor="http://localhost:4444",
        options=driver_options
        )
        driver.get('https://lx.uts.edu.au/')
        driver.maximize_window()
        return driver

def click_right_arrow(driver):
        right_arrow = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/section[1]/div/div/button[2]')
        driver.execute_script("arguments[0].click();", right_arrow)

def click_left_arrow(driver):
        left_arrow = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/section[1]/div/div/button[1]')
        driver.execute_script("arguments[0].click();", left_arrow)

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
                WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/section/div/div[2]/div[1]/div[2]/div/h3/a"))).click()
                home_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img")
                driver.execute_script("arguments[0].click();", home_button)
                #End of search bar

                #Slick Arrows top
                click_left_arrow(driver)
                click_right_arrow(driver)
                article = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/section[1]/div/div/div/div/div[2]/div[2]/a')
                driver.execute_script("arguments[0].click();", article)
                home_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img")
                driver.execute_script("arguments[0].click();", home_button)

                click_right_arrow(driver)
                click_left_arrow(driver)
                # find the article to the left
                article_left = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/section[1]/div/div/div/div/div[4]/div[2]/a')
                driver.execute_script("arguments[0].click();", article_left)
                home_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img")
                driver.execute_script("arguments[0].click();", home_button)
                
                click_right_arrow(driver)
                click_left_arrow(driver)
                # find the article to the right
                article_right = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[2]/section[1]/div/div/div/div/div[3]/div[2]/a')
                driver.execute_script("arguments[0].click();", article_right)
                home_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[1]/a/img")
                driver.execute_script("arguments[0].click();", home_button)
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
                print(driver.current_url)
                driver.quit() #KILL IT! (WITH FIRE)