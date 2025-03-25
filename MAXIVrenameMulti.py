

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:13:36 2024

@author: ratjan
"""

import pandas as pd
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename,askopenfilenames
from tkinter.filedialog import askdirectory
import re
import shutil



#%%
def get_datatable():
    fn = askopenfilename(title='Scanlog datatable') # Open scanlog datatable
    print("User chose", fn)
    if fn:  # Check if a file is selected
        df = pd.read_csv(fn, sep=';')
        return df
    else:
        print("No file selected.")
        return None

# Call the function and store the returned DataFrame
df = get_datatable()

# Check if the DataFrame is successfully loaded
if df is not None:
    print(df.head())  # Example: Print first 5 rows of the DataFrame
#%%
def check_ScanID(numstr, df):
   for scan_id in df['ScanID'].values:
        if numstr == scan_id:
            return df[df['ScanID'] == numstr].iloc[0]
   return None
    
#%%  
def main():



    file_paths = askopenfilenames(title='Files to process')     # Ask user to select multiple files
    print("User chose", len(file_paths), "file(s)")
    save_folder_path = askdirectory(title='Save directory')             # Ask user to select a destination folder
    for fn2 in file_paths:
        filename = os.path.basename(fn2)
        print("Processing:", filename)

        # Perform operations on selected file
        numbers = [int(num) for num in re.findall(r'\d+', filename)]  # Find all numbers in file name
        numstr = int(''.join(map(str, numbers)))  # Join numbers into a single integer
        result = check_ScanID(numstr, df)  # Calls function
        if result is not None:
            torename = result['description']+"-" + filename
            torename = torename.replace(" ", "").replace('/', '-') #rename data file
            print(result)
            print(torename)


            
            destination_filename = f"{torename}.dat"
            save_dest = os.path.join(save_folder_path, destination_filename)
            save_dest1 = save_dest.replace('\\', '/') #Create file path

            shutil.copy(fn2, save_dest1) #Copy and rename
            print(f"File copied to {save_dest1}")
        else:
            print("Scan ID not found in dataframe.")
if __name__ == "__main__":
    main()

