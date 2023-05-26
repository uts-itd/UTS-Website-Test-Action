from selenium import webdriver
from selenium_website_test import set_options, setup_driver, webtest
firefox_options = webdriver.FirefoxOptions()
set_options(firefox_options)
driver_firefox = setup_driver(firefox_options)
webtest(driver_firefox)