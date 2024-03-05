from PIL import Image
import os

# مسیر پوشه ای که تصاویر رویی در آنجا قرار دارند
source_directory = r"C:\\Users\\ehsan\Desktop\\طراحی سایت\\bitic\\ickalabbg\\"

# مسیر پوشه ای که تصاویر نهایی در آنجا ذخیره خواهند شد
destination_directory = r"C:\\Users\\ehsan\\Desktop\\طراحی سایت\\bitic\\khoroji\\"

# باز کردن تصویر اصلی (پس‌زمینه)
background_image_path = r"C:\\Users\\ehsan\\Desktop\\طراحی سایت\\bitic\\goooz.png"
img1 = Image.open(background_image_path)

# لیست کردن فایل‌های موجود در پوشه مبدا
image_files = os.listdir(source_directory)

# باز کردن هر تصویر رویی، اعمال تغییرات و ذخیره آن در پوشه مقصد
for image_file in image_files:
    # باز کردن تصویر اصلی هر بار برای اعمال تغییرات جدید بر روی آن
    img_copy = img1.copy()

    # باز کردن تصویر رویی
    img2 = Image.open(source_directory + image_file)

    # اعمال تغییرات روی تصویر
    img_copy.paste(img2, (0, 0), mask=img2)

    # ذخیره تصویر نهایی با همان نام در پوشه مقصد
    img_copy.save(destination_directory + image_file)

    # بستن تصویر رویی
    img2.close()

# بستن تصویر اصلی (پس‌زمینه)
img1.close()
