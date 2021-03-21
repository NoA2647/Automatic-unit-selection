# Hello , this program get study from portal of aut automatically
from selenium import webdriver
import json
from selenium.common.exceptions import NoSuchElementException
import time


def read_config():
    with open('./config.txt', 'r') as f:
        return json.load(f)


config = read_config()
userName = config['userName']
password = config['password']
listens = config['listens']
driver = webdriver.Chrome()  # open chrome
driver.get("https://portal.aut.ac.ir/aportal/")  # go to this url
while True:
    id_box = driver.find_element_by_name('username')
    id_box.send_keys(userName)  # Enter the student number
    id_box = driver.find_element_by_id('password')
    id_box.send_keys(password)  # Enter the password
    id_box = driver.find_element_by_id('passline')
    id_box.click()  # click on blank captcha
    while True:
        if len(id_box.get_attribute("value")) == 5:
            break
    driver.find_element_by_class_name('logbutton').click()  # log in
    try:
        driver.find_element_by_xpath('/html/body/table')
        time.sleep(1)
    except NoSuchElementException:
        break
frame = driver.find_element_by_name("side")
driver.switch_to_frame(frame)
id_box = driver.find_element_by_xpath("//div[@id='Bar_panel0_b1']").click() #click on akhz shode
frame = driver.find_element_by_name("main")
driver.switch_to_frame(frame)
time.sleep(1)  # waiting to load
for listen in listens:
    id_box = driver.find_element_by_name('st_reg_courseid')
    id_box.send_keys(listen["listenId"])  # Enter code of study
    id_box = driver.find_element_by_name('st_reg_groupno')
    id_box.send_keys(listen["groupId"])  # Enter group of study
    id_box = driver.find_element_by_name('addpassline')
    id_box.click()
    while True:
        if len(id_box.get_attribute("value")) == 2:
            break
    driver.find_element_by_name('st_course_add').click()
    time.sleep(0.5)  # waiting to load
driver.save_screenshot("./screenShot.png")  # get screenshot & saved in <dir>
