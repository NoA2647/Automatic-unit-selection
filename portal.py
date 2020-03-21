#Hello , this program get study from portal of aut automaticly
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()#open firefox
driver.get("https://portal.aut.ac.ir/aportal/")#go to this url
id_box = driver.find_element_by_name('username')
id_box.send_keys('*******')#Enter the student number
id_box = driver.find_element_by_id('password')
id_box.send_keys('*******')#Enter the password
id_box = driver.find_element_by_id('passline')
id_box.click()
time.sleep(5)#waiting to enter pass-picture  
id_box = driver.find_element_by_class_name('logbutton')
id_box.click()
driver.switch_to_default_content()
frame = driver.find_element_by_name("side")
driver.switch_to_frame(frame)
id_box = driver.find_element_by_xpath("//div[@id='Bar_panel0_b1']")
id_box.click()
driver.switch_to_default_content()
frame = driver.find_element_by_name("main")
driver.switch_to_frame(frame)
time.sleep(0.05)#waiting to load
id_box = driver.find_element_by_name('st_reg_courseid')
id_box.send_keys('*******')#Enter code of study
id_box = driver.find_element_by_name('st_reg_groupno')
id_box.send_keys('*******')#Enter group of study
id_box = driver.find_element_by_name('addpassline')
id_box.click()
time.sleep(2)#waiting for enter pass-picture
id_box = driver.find_element_by_name('st_course_add')
id_box.click()
time.sleep(0.05)#waiting to load
driver.save_screenshot("*******")#get screenshot & saved in <dir>
