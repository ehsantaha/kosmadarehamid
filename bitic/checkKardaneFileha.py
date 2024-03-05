import os

def list_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.splitext(file)[0])
    return file_list

def find_duplicate_files(directory1, directory2):
    files1 = set(list_files(directory1))
    files2 = set(list_files(directory2))
    duplicates = files1.intersection(files2)
    return files1.union(files2) - duplicates

directory1 = "C:\\Users\\ehsan\\Desktop\\طراحی سایت\\bitic\\New folder\\New folder"
directory2 = "E:\\bedoneBG-IC"

unique_files = find_duplicate_files(directory1, directory2)

for file in unique_files:
    print(file)
