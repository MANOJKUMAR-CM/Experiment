import os
import shutil

source_path = r'D:\MUSIC\Experiment1\Carnatic'
dest_path = 'D:/MUSIC/Experiment1/Data'

if not os.path.exists(dest_path):
    os.makedirs(dest_path)

# Create a list of files to move
files_to_move = [file for file in os.listdir(source_path) if file.endswith('.trans12_pitchextrm')]

for file in files_to_move:
    source_path1 = os.path.join(source_path, file)
    source_path1 = source_path1.replace('\\', '/')
    
    destination_path = os.path.join(dest_path, file)
    destination_path = destination_path.replace('\\', '/')
    
    shutil.copy(source_path1, destination_path)

print("Files have been moved to the new folder.")
