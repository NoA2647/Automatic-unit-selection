from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://internet.aut.ac.ir")
id_box = driver.find_element_by_name('username')
id_box.send_keys('amir.h.j')
id_box = driver.find_element_by_name('password')
id_box.send_keys('ubuntu6276')
id_box = driver.find_element_by_id('internetbutton')
id_box.click()
