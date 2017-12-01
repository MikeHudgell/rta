#
# load all RTA data into a dataframe, translate reference data and save to csv.
# each years worth of data is in a subdirectory
#

import os
import zipfile

data_dir = "/media/mike/HDD/git/rta/raw_data"
output_dir = "/media/mike/HDD/git/rta/unzipped_data"

# work out how many years worth of data we are dealing with and create list of years
files_in_data_dir = os.listdir(data_dir)
subfolders = []
for file in files_in_data_dir:
    if os.path.isdir(os.path.join(data_dir, file)):
        subfolders.append(file)
print(len(subfolders))

# go through each year and unzip files
for dir in subfolders:
    os.makedirs((os.path.join(output_dir, dir)), exist_ok=True)
    files_in_year_dir = os.listdir(os.path.join(data_dir, dir))
    for file in files_in_year_dir:
        zipref = zipfile.ZipFile(os.path.join(data_dir, dir, file))
        zipref.extractall(os.path.join(output_dir, dir))
        zipref.close()

# go through all unzipped files and rename so we have a common pattern across years.
for dir in subfolders:
    source_dir = os.path.join(output_dir, dir)
    files_in_source_dir = os.listdir(source_dir)
    for file in files_in_source_dir:
        if "Make" in file:
            os.rename(os.path.join(source_dir, file) , os.path.join(source_dir, "make_model.csv"))
        if "Accidents" in file:
            os.rename(os.path.join(source_dir, file) , os.path.join(source_dir, "accidents.csv"))
        if "Veh" in file and "Make" not in file:
            os.rename(os.path.join(source_dir, file) , os.path.join(source_dir, "vehicles.csv"))
        if "Cas" in file:
            os.rename(os.path.join(source_dir, file) , os.path.join(source_dir, "casualties.csv"))

