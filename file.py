import os
import shutil
import pandas as pd

src='D:/MUSIC/Experiment1/Data'
dest='D:/MUSIC/Experiment1/Data'

#Create a list of files to move
files_to_move = [file for file in os.listdir(src) if file.endswith('.trans12_pitchextrm')]

for file_name in files_to_move:
    source_file_path = os.path.join(src, file_name)
    dest_file_path = os.path.join(dest, f'{os.path.splitext(file_name)[0]}.Embedded12')
    
    df = pd.read_csv(source_file_path, delimiter='\s+', header=None)
    
    calculated_column = 12 * (df.iloc[:, 2] - 1) + df.iloc[:, 1]
    
    new_df = pd.DataFrame({
        0: df.iloc[:, 0],          
        1: calculated_column,      
        2: df.iloc[:, 3]           
    })

    # Write the new DataFrame to the destination file
    new_df.to_csv(dest_file_path, sep='\t', header=False, index=False)

print("Files have been processed and new files created.")