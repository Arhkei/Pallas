# Usage:
# Put into root directory of Prelude's community repo (https://github.com/preludeorg/community)
# Type in folder name to catgeorize (ex. discovery)
# Results will be in the sorted folder and be seperated by OS making them ready to be imported into Pallas
##########################
import yaml
import os
from shutil import copyfile, rmtree

cwd = os.getcwd()
rmtree (f"{cwd}\\sorted")
os.mkdir(f"{cwd}\\sorted")
os.mkdir(f"{cwd}\\sorted\\darwin")
os.mkdir(f"{cwd}\\sorted\\global")
os.mkdir(f"{cwd}\\sorted\\linux")
os.mkdir(f"{cwd}\\sorted\\windows")
category = input("Enter category name: ")
os.chdir(f".\\{category}")
for file in os.listdir():
    with open(file, 'r',encoding="utf8") as f:
        submoduleInfo = yaml.load(f, Loader=yaml.FullLoader)
        name = submoduleInfo['name']
        print(name)
        for platform in submoduleInfo['platforms']:
            copyfile(file, f"..\\sorted\\{platform}\\{name}.yml")
            print(platform)
        print("\n")
