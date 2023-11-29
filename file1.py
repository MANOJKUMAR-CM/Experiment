import os
import pandas as pd

source_path = 'D:/MUSIC/Experiment1/Data'
dest_path = 'D:/MUSIC/Experiment1/Data'

files_to_process = [file for file in os.listdir(source_path) if file.endswith('.Embedded12')]

middle_columns_list = []

for file_name in files_to_process:
    file_path = os.path.join(source_path, file_name)

    df = pd.read_csv(file_path, sep='\t', header=None)

    middle_column_index = len(df.columns) // 2
    
    middle_column = df.iloc[:, middle_column_index].astype(int)
    middle_columns_list.append(middle_column)

result_df = pd.concat(middle_columns_list, axis=0,ignore_index=True)
print(result_df.shape)

result_file_path = os.path.join(dest_path, 'all_middle_columns.txt')
result_df.to_csv(result_file_path, sep='\t', header=False, index=False)

print("Middle columns have been concatenated into a new file:", result_file_path)
