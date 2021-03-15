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
import csv
import random
import numpy as np

#Settings

file_name_head = "testdata_"
file_name_end = ""
file_ext = ".txt"

data_name_head = "data_"
data_name_end = ""

value_name_head = "value_"
value_name_end = ""

target_name = "target"

index_name = "dataname"

no_files = 1
rows = 10
columns = 5

target_val = [0, 1]

random_range = [0, 99]
nan_val = range(100, 101)

# +
#Main

for no_file in range(no_files):
    filename = file_name_head + str(no_file + 1) + file_name_end + file_ext
#     print(filename)
    f = open(filename, "w")
    writer = csv.writer(f)
    
    header = [index_name]
    for column in range(columns):
        valuename = value_name_head + str(column + 1) + value_name_end
        header.append(valuename)
        
    if len(target_val) > 1:
        header.append(target_name)
        
    writer.writerow(header)
    
    for row in range(rows):
        data = []
        dataname = data_name_head + str(row + 1) + data_name_end
        data.append(dataname)
        
        for column in range(columns):
            random_val = random.randint(random_range[0], random_range[1])
            if random_val in nan_val:
                random_val = np.nan
                
            print(random_val)
            data.append(random_val)
                
        if len(target_val) > 1:
            data.append(random.choice(target_val))
                
        writer.writerow(data)
    
    f.close()
    
print("Done")
# -




