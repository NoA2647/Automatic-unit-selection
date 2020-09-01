#Hello , this program get study from portal of aut automaticly
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

userName = "" # enter user name
password = "" # enter password
listens = [{"listenId":"","groupId":""}] #enter listen id and group id like this ,its dictionery
driver = webdriver.Firefox() #open firefox
driver.get("https://portal.aut.ac.ir/aportal/") #go to this url
id_box = driver.find_element_by_name('username')
id_box.send_keys(userName) #Enter the student number
id_box = driver.find_element_by_id('password')
id_box.send_keys(password) #Enter the password
id_box = driver.find_element_by_id('passline')
#print(id_box)
id_box.click()
time.sleep(5) #waiting to enter pass-picture  
id_box = driver.find_element_by_class_name('logbutton')
id_box.click()
driver.switch_to_default_content()
frame = driver.find_element_by_name("side")
driver.switch_to_frame(frame)
id_box = driver.find_element_by_xpath("//div[@id='Bar_panel1_c']")
id_box.click()
id_box = driver.find_element_by_xpath("//div[@id='Bar_panel1_b0']")
id_box.click()
driver.switch_to_default_content()
frame = driver.find_element_by_name("main")
driver.switch_to_frame(frame)
time.sleep(1) #waiting to load
for listen in listens:
    id_box = driver.find_element_by_name('st_reg_courseid')
    id_box.send_keys(listen["listenId"]) #Enter code of study
    id_box = driver.find_element_by_name('st_reg_groupno')
    id_box.send_keys(listen["groupId"]) #Enter group of study
    id_box = driver.find_element_by_name('addpassline')
    id_box.click()
    time.sleep(2) #waiting for enter pass-picture
    id_box = driver.find_element_by_name('st_course_add')
    id_box.click()
    time.sleep(0.5) #waiting to load
driver.save_screenshot("./screenShot.png") #get screenshot & saved in <dir>