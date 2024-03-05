from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import pyautogui
import os
import keyboard

folder_path = r"Z:\picture"
    # پیدا کردن تمامی فایل‌های عکس در پوشه
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

source_directory = r"C:\Users\Hamidreza\Downloads"
destination_directory = r"C:\Users\Hamidreza\Desktop\nnn"
timeout = 50


for image_file in image_files:
    print(image_file)
        # وارد کردن مسیر عکس
    input_path = os.path.join(folder_path, image_file)

    # راه‌اندازی مرورگر Chrome
    driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver-win32\chromedriver.exe")

    # باز کردن صفحه وب
    driver.get("https://dewatermark.ai/")

    try:
        # صبر کردن تا المان قابل کلیک باشد
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/button'))
        )

        # کلیک کردن بر روی المان
        element.click()
        time.sleep(3)
        keyboard.write(input_path)
        keyboard.press_and_release('enter')

        # صبر کردن تا المان مورد نظر بر روی صفحه ظاهر شود
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/div[2]/div[2]'))
        )

        # کلیک کردن بر روی المان دیگر
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/div[2]/div[2]').click()

        # صبر کردن تا المان مورد نظر دیگر ظاهر شود
        WebDriverWait(driver, 50).until(
        EC.staleness_of(driver.find_element(By.XPATH, ' //*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div/div[1]/div/div/div')))


        # Wait for the button to be visible and clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download")]'))  # Adjust XPath if needed
        )
        # Click the button
        driver.execute_script("arguments[0].click();", button)


        start_time = time.time()
        file_moved = False
        while time.time() - start_time <= timeout:
            files = os.listdir(source_directory)
            for file in files:
                source_path = os.path.join(source_directory, file)
                if os.path.isfile(source_path) and file.lower().endswith('.jpeg'):
                    # New filename
                    new_filename = image_file
                    destination_path = os.path.join(destination_directory, new_filename)
                    os.rename(source_path, destination_path)
                    print(f"File {file} moved successfully to {new_filename}.")
                    file_moved = True
                    break  # Exit the inner for loop
            if file_moved:
                break  # Exit the outer while loop
            time.sleep(1)

        if not file_moved:
            print("Timeout reached. No new jpg file created.")
    finally:
        # در پایان بستن مرورگر
        driver.quit()