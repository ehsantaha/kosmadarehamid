from PIL import Image
import os

def check_image_dimensions(input_folder, target_width=1500, target_height=1500):
    incorrect_dimensions = []

    # Iterate over all items in the input folder
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            input_path = os.path.join(root, file)

            # Read the image
            try:
                image = Image.open(input_path)
            except Exception as e:
                print(f"Error opening {input_path}: {e}")
                continue

            # Check image dimensions
            width, height = image.size
            if width != target_width or height != target_height:
                incorrect_dimensions.append(input_path)

    return incorrect_dimensions

input_folder = "E:\\bedoneBG-IC"

incorrect_images = check_image_dimensions(input_folder)
print("Images with incorrect dimensions:", incorrect_images)
