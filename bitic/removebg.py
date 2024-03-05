from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import os
import keyboard

driver = webdriver.Chrome()
    # باز کردن صفحه وب
driver.get("https://create.pixelcut.ai/")

time.sleep(120)
print("kos madare hamid")

def process_images(images):
    
    # باز کردن صفحه وب
    driver.get("https://create.pixelcut.ai/")

    try:
        # وارد کردن مسیر عکس‌ها به صورت یکجا
        input_paths = ' '.join(['"{}"'.format(os.path.join(folder_path, image_file)) for image_file in images])
        print(input_paths)

        # صبر کردن تا المان قابل کلیک باشد
        imgbgremove = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div/div/div/div/div/section[1]/div/a[1]/img'))
        )
        imgbgremove.click()
        


        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div/div/main/div/div/div[2]/div/div[1]/button[1]'))
        )

        # کلیک کردن بر روی المان
        element.click()
        time.sleep(3)

        keyboard.write(input_paths)
        keyboard.press_and_release('enter')

        # # صبر کردن تا المان مورد نظر بر روی صفحه ظاهر شود
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/div[2]/div[2]'))
        # )
        
        # # کلیک کردن بر روی المان دیگر
        # driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/div[2]/div[2]').click()

        # صبر کردن تا المان مورد نظر دیگر ظاهر شود
        WebDriverWait(driver, 1000000).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div/div[1]/div'))
        )

        # انجام عملیات کلیک بر روی المان دوم
        while True:
            try:
                # چک کردن حضور المان دوم
                element_2 = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/main/div[2]/ol/li/div/div/button'))
                )
                # اگر المان دوم موجود است و المان اول هم هنوز موجود است، کلیک کنید و سپس منتظر المان اول بمانید
                if element_2:
                    element_2.click()
                    # منتظر شدن برای حضور المان اول
                    WebDriverWait(driver, 1000000).until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div/div[1]/div'))
                    )
            except:
                # اگر المان دوم دیگر وجود ندارد، از حلقه خارج شوید
                break

        # Wait for the button to be visible and clickable
        # button2 = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download all")]'))  # Adjust XPath if needed
        # )
        # # Click the button
        # driver.execute_script("arguments[0].click();", button2)
            
        # Wait for the button to be clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Download all')]"))
        )
        
        # Click on the button
        button.click()

        time.sleep(10)

        WebDriverWait(driver, 1000000).until(
            EC.invisibility_of_element_located((By.XPATH, '//*[@id="radix-27"]/div/div'))
            )
        
        time.sleep(10)

    finally:
        
        driver.get("https://create.pixelcut.ai/")

folder_path = r"C:\Users\ehsan\Desktop\pictures"
# پیدا کردن تمامی فایل‌های عکس در پوشه
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# تقسیم لیست عکس‌ها به گروه‌های 500 تایی
for i in range(0, len(image_files), 500):
    images_group = image_files[i:i+500]
    process_images(images_group)

driver.quit()