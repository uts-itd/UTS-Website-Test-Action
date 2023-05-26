from selenium import webdriver
from browser_test.selenium_website_test import set_options, setup_driver, webtest
chrome_options = webdriver.ChromeOptions()
set_options(chrome_options)
driver_chrome = setup_driver(chrome_options)
webtest(driver_chrome)