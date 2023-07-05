import os
import shutil

source_dir = input("Enter path of the source")
destination_dir = input("Enter path of destination")

def organize_files():
    for filename in os.listdir(source_dir):

        file_path = os.path.join(source_dir, filename)
        
        if not os.path.isfile(file_path) or filename.startswith('.'):
            continue
        
        file_extension = os.path.splitext(filename)[1][1:].lower()
        
        dest_directory = os.path.join(destination_dir, file_extension)
        os.makedirs(dest_directory, exist_ok=True)
        
        shutil.move(file_path, os.path.join(dest_directory, filename))

organize_files()