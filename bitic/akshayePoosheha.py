import os
import shutil

def copy_images_from_subdirectories(source_dir, destination_dir):
    # لیست کردن پوشه‌های داخلی در مسیر منبع
    subdirectories = [subdir for subdir in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, subdir))]
    
    for subdir in subdirectories:
        subdir_path = os.path.join(source_dir, subdir)
        # بدست آوردن لیست تمام فایل‌ها در هر زیرپوشه
        files = [file for file in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, file))]
        if len(files) > 0:
            # انتخاب یک فایل از هر زیرپوشه
            selected_file = os.path.join(subdir_path, files[0])
            # کپی کردن فایل انتخاب شده به پوشه مقصد
            shutil.copy(selected_file, os.path.join(destination_dir, subdir + ".jpg"))

# مسیر پوشه منبع (پوشه حاوی زیرپوشه‌ها با عکس‌ها)
source_directory = "C:\\Users\\ehsan\\Desktop\\tekrari\\yekJa"
# مسیر پوشه مقصد (پوشه برای ذخیره عکس‌های انتخاب شده با نام زیرپوشه‌ها)
destination_directory = "C:\\Users\\ehsan\\Desktop\\tekrari\\nahaii"

# فراخوانی تابع برای کپی کردن عکس‌ها
copy_images_from_subdirectories(source_directory, destination_directory)
