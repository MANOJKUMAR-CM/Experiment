import pandas as pd
import numpy as np

src='D:/MUSIC/Experiment1/Data/all_middle_columns.txt'
df = pd.read_csv(src, header=None)
unique_values = df[0].unique()
one_hot_encoding = pd.get_dummies(df[0], prefix='one_hot')
one_hot_array = one_hot_encoding.to_numpy()

result_df = pd.DataFrame({
    'number': df[0],
    'one_hot_array': list(one_hot_array)
})
print(result_df)

