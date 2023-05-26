from selenium import webdriver
from browser_test.selenium_website_test import set_options, setup_driver, webtest
edge_options = webdriver.EdgeOptions()
set_options(edge_options)
driver_edge = setup_driver(edge_options)
webtest(driver_edge)