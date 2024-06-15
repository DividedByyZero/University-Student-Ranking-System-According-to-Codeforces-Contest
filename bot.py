from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip

options = Options()
options.add_experimental_option("detach",True)
def send_message(messages):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    time.sleep(1)
    email = driver.find_element("xpath","/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
    # emain id of your facebook account
    email.send_keys('email@email.com')
    password = driver.find_element("xpath","/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
    # password of your facebook account
    password.send_keys('password')
    submit = driver.find_element("xpath","/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
    submit.click()
    # driver.execute_script("window.open('about:blank', '_blank');")
    # driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    # group chat link where you send messages
    driver.get("https://www.facebook.com/messages/t/group_id")
    time.sleep(5)
    message = driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]/p')
    for line in messages:    
        pyperclip.copy(line)
        time.sleep(10)
        # message = driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]/p')
        message.send_keys(Keys.CONTROL,'v')
        message.send_keys(Keys.SHIFT, Keys.ENTER)
        print(line)
    
    message.send_keys(Keys.ENTER)
    time.sleep(5)
    print("send message!")

