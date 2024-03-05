import os
import shutil

def split_files(source_folder, destination_folder, batch_size=100):
    files = os.listdir(source_folder)
    file_batches = [files[i:i+batch_size] for i in range(0, len(files), batch_size)]
    
    for i, batch in enumerate(file_batches):
        batch_folder = os.path.join(destination_folder, f"batch_{i+1}")
        os.makedirs(batch_folder, exist_ok=True)
        
        for file in batch:
            source_file_path = os.path.join(source_folder, file)
            destination_file_path = os.path.join(batch_folder, file)
            shutil.move(source_file_path, destination_file_path)

source_folder = "C:\\Users\\ehsan\\Desktop\\طراحی سایت\\bitic\\New folder\\pictures"
destination_folder = "C:\\Users\\ehsan\\Desktop\\طراحی سایت\\bitic\\New folder\\New folder (2)"

split_files(source_folder, destination_folder, batch_size=100)
