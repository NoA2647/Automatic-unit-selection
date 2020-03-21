from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://samad.aut.ac.ir")
id_box = driver.find_element_by_id('username')
id_box.send_keys('9713042')
id_box = driver.find_element_by_id('password')
id_box.send_keys('amir2647')
id_box = driver.find_element_by_id('login_btn_submit')
id_box.click()
driver.get("https://samad.aut.ac.ir/nurture/user/multi/reserve/showPanel.rose?selectedSelfDefId=1")
time.sleep(2)
id_box = driver.find_element_by_id('nextWeekBtn')
id_box.click()