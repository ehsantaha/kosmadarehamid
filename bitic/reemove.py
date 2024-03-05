from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import os
import pickle


# راه‌اندازی مرورگر Chrome
driver = webdriver.Chrome()

    # باز کردن صفحه وب
driver.get("https://create.pixelcut.ai/")

cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    cookie['domain'] = ".pixelcut.ai"
        
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        pass

driver.get('https://create.pixelcut.ai/account')

time.sleep(120)