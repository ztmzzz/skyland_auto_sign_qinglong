import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def getDid():
    options = Options()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)

    file_path = 'file://' + os.path.abspath('./index.html')  # 替换为你的HTML文件路径
    driver.get(file_path)

    time.sleep(2)

    button = driver.find_element(By.ID, 'getDeviceId')
    button.click()

    time.sleep(2)

    textbox = driver.find_element(By.ID, 'deviceIdOutput')
    textbox_value = textbox.get_attribute('value')

    driver.quit()

    return textbox_value
