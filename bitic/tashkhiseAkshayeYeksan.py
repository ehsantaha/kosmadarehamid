import os
import shutil
from PIL import Image
import hashlib

def get_image_hash(image_path):
    image = Image.open(image_path)
    bw_image = image.convert('L')
    image_hash = hashlib.md5(bw_image.tobytes()).hexdigest()
    return image_hash

def organize_images(source_dir, destination_dir):
    file_list = os.listdir(source_dir)
    image_counts = {}
    
    for filename in file_list:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                image_hash = get_image_hash(os.path.join(source_dir, filename))
                if image_hash in image_counts:
                    image_counts[image_hash].append(filename)
                else:
                    image_counts[image_hash] = [filename]
            except Exception as e:
                print(f"Error processing image {filename}: {e}")
    
    for hash_value, filenames in image_counts.items():
        if len(filenames) > 1:
            hash_dir = os.path.join(destination_dir, hash_value)
            os.makedirs(hash_dir, exist_ok=True)
            for filename in filenames:
                shutil.move(os.path.join(source_dir, filename), hash_dir)

# فراخوانی تابع برای سازماندهی تصاویر
organize_images("E:\\bedoneBG-IC", "E:\\bedoneBG-IC")