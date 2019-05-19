#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def wait_until_user_exits():
    should_exit = False
    while not should_exit:
        try:
            time.sleep(10)
            should_exit = driver.window_handles.__len__() == 0
        except Exception as e:
            should_exit = True


#Path to chromedriver
#If you followed the tutorial until now it should be located at ./chromedriver
chromedriver_path = "./chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver_path)

#The website url you want to manipulate with selenium
url = "https://forvo.com/login"
driver.get(url)

#Example of finding elements
login_elem = driver.find_element_by_css_selector("input#login.focus")
password_elem = driver.find_element_by_css_selector("input#password")

#Example of entering keys into elements
login_elem.send_keys("mylogin@login.com")
password_elem.send_keys("securepassword")
password_elem.send_keys(Keys.RETURN)

#Prevent selenium from shutting down until all browsers are terminated by user
wait_until_user_exits()

#close all selenium related processes
driver.quit()
