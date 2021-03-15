# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import pandas as pd
import random
import numpy as np

#Settings

file_name_head = "testdata_"
file_name_end = ""
file_ext = ".csv"

column_name_head = "value_"
column_name_end = ""

index_name_head = "data_"
index_name_end = ""

target_name = "target"

no_files = 3
no_indexes = 10
no_columns = 5

target_val = [0, 1]
random_range = range(0, 100)
nan_val = range(100, 101)


# +
#Main

for no_file in range(no_files):
    filename = file_name_head + str(no_file + 1) + file_name_end + file_ext
#     print(filename)
    column_name_list = [column_name_head + str(i + 1) + column_name_end for i in range(no_columns)]
#     print(column_name_list)
    index_name_list = [index_name_head + str(i + 1) + index_name_end for i in range(no_indexes)]
#     print(index_name_list)
    df = pd.DataFrame(index=index_name_list, columns=column_name_list)
#     print(df)
    for column in column_name_list:
        df[column] = random.choices(random_range, k=no_indexes)
#     print(df)
    for i in nan_val:
        df = df.replace(i, np.nan)
    
    df[target_name] = random.choices(target_val, k=no_indexes)
    
    df.to_csv(filename)
# -


