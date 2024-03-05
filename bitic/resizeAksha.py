from PIL import Image
import os

def resize_images(input_folder, output_folder, target_width=1500, target_height=1500):
    os.makedirs(output_folder, exist_ok=True)
    files = os.listdir(input_folder)
    
    for file in files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)
        
        # خواندن تصویر
        image = Image.open(input_path)
        
        # تغییر اندازه تصویر با حفظ فرمت و کیفیت
        resized_image = image.resize((target_width, target_height), Image.LANCZOS)
        
        # ذخیره تصویر تغییر اندازه‌داده شده
        resized_image.save(output_path)

input_folder = "C:\\Users\\ehsan\\Desktop\\New folder"
output_folder = "C:\\Users\\ehsan\\Desktop\\dddd"

resize_images(input_folder, output_folder)
