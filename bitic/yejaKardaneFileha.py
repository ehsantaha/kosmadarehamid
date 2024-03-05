import os
import shutil

def copy_files(src_dir, dest_dir):
    # چک کردن وجود مسیر مقصد و در صورت نبودن آن، ایجاد آن
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # پیمایش تمام زیرپوشه‌ها و فایل‌ها در مسیر مبدا
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_file_path = os.path.join(root, file)
            # مقصد فایل در مسیر مقصد
            dest_file_path = os.path.join(dest_dir, file)
            # کپی کردن فایل به مسیر مقصد
            shutil.copy(src_file_path, dest_file_path)
            print(f"Copied {src_file_path} to {dest_file_path}")

# تعیین مسیر مبدا و مقصد
source_directory = "C:\\Users\\ehsan\\Desktop\\طراحی سایت\\bitic\\New folder\\New folder (2)"
destination_directory = "C:\\Users\\ehsan\\Desktop\\طراحی سایت\\bitic\\New folder\\yekJa"

# فراخوانی تابع برای کپی فایل‌ها
copy_files(source_directory, destination_directory)
