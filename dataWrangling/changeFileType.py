
# Import Module
import os
import json
  
# Folder Path
path = "C:/Users/apers/partXpush_data/data"
  
# Change the directory
os.chdir(path)
  
# Read text File
  
    # iterate through all file
i = 1
for file in os.listdir(path=path):
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        print(file_path)
        with open(file, "r") as data:
            # remove any old .json files
            #os.remove(f"{path}/{file}.json")
            # write .txt files to .json line by line
            with open(f"{path}/{i}.json", "w") as output:
                for line in data.readlines():
                    output.write(line)
    i += 1
