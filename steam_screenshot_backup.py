import os
import sys
import getopt
from shutil import copy2


def interate_directory(path):
    dir = os.listdir(path)
    for folder_or_file in dir:
        if os.path.isdir(os.path.join(path, folder_or_file)):
            if folder_or_file == "screenshots":
                for file in os.listdir(os.path.join(path, folder_or_file)):
                    if os.path.isfile(os.path.join(path, folder_or_file, file)) and file != "thumbnails":
                        print(
                            f"{os.path.join(path,folder_or_file,file)} to {os.path.join(target_path,file)}")
                        copy2(os.path.join(path, folder_or_file, file),
                              os.path.join(target_path, file))
            # print(f"{folder_or_file} is a directory")
            interate_directory(os.path.join(path, folder_or_file))


opts, args = getopt.getopt(sys.argv[1:], 's:t:', [
                           'steamfolder=', 'targetfolder='])

source_path = None
target_path = None

for opt, arg in opts:
    if opt in ('-s', '--steamfolder'):
        source_path = arg
    if opt in ('-t', '--targetfolder'):
        target_path = arg

# check if params are present
try:
    assert source_path != None, "Please provide a path to your steam folder like this: --steamfolder 'C:/Games/Steam'"
    assert target_path != None, "Please provide a path to the destination where the screenshots are supposed to be saved to like this: 'C:/Users/Oshimani/Pictures/SteamScreenshots'"
except AssertionError as ae:
    print(ae)
    exit()

# check if directories are valid
try:
    assert os.path.isdir(
        source_path), f"{source_path} is not a valid directory."
    assert os.path.isdir(
        target_path), f"{target_path} is not a valid directory."
except AssertionError as ae:
    print(ae)
    exit()

# start searching
print(f"Starting to gather screenshots from {source_path}")
source_path = os.path.join(source_path, "userdata")
try:
    assert os.path.isdir(source_path), f"No screenshots at {source_path}"
except AssertionError as ae:
    print(ae)
    exit()

interate_directory(source_path)
