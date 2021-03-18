from lib.colored_print import colors
import os
from os.path import expanduser
import time
import sys
from sys import platform as _platform
import yaml

if _platform == "linux" or _platform == "linux2":
    osInfo = "linux"
    CLEAR = "clear"
elif _platform == "darwin":
    osInfo = "darwin"
    CLEAR = "clear"
elif _platform == "win32" or _platform == "win64":
    osInfo = "windows"
    CLEAR = "cls"
else:
    colors.cprint(colors.RED, "OS not detected")
    colors.cprint(colors.RED, "Exiting...")
    sys.exit()


def setup():

    # Gathers the two differnt logos
    with open("lib/full_logo.txt", "r") as f:
        full_logo = "".join(f.readlines())

    with open("lib/partial_logo.txt", "r") as f:
        partial_logo = "".join(f.readlines())

    # Cycles through each logo for animation
    for i in range(3):
        print(partial_logo)
        time.sleep(0.5)
        os.system(CLEAR)
        print(full_logo)
        time.sleep(0.5)
        if i != 2:
            os.system(CLEAR)
        else:
            print("\n\n\n")


def submoduleHelp():
    print("Commands")
    print("\t<submodule number> --id\n\t\tShows TTP ID")
    print("\t<submodule number> --authors\n\t\tShows authors")
    print("\t<submodule number> --name\n\t\tShows original name")
    print("\t<submodule number> --desc\n\t\tShows description")
    print("\t<submodule number> --platforms\n\t\tShows other available platforms")
    print("\t<submodule number> --command\n\t\tSaves output to file")
    print("\tq\n\t\tPress q to quit to modules")


def moduleChoice():
    modules = {}
    colors.cprint(colors.BLUE, "\n\nModules:")
    #Traverses tbe module directory and prints out the folders (submodules)
    for index, file in enumerate(os.listdir('.\\modules')):
        d = os.path.join('.\\modules', file)
        if os.path.isdir(d):
            colors.cprint(colors.GREEN, f"\t{index+1}: {file}")
            modules[index+1] = file

    choice = input("\nEnter module number: ")
    submoduleHelp()
    module = modules[int(choice[0:2])]
    os.chdir(f".\\modules\\{module}\\" + osInfo)
    files = os.listdir()

    submoduleChoice(files)


def submoduleChoice(files):
    choice = ""
    while choice != 'q':
        colors.cprint(colors.BLUE, "\nSubmodules: ")
        #Prints the submodules in the chosen module
        for index, file in enumerate(files):
            colors.cprint(colors.GREEN, f"\t{index+1}. {file[:-4]}")
        choice = input("\nEnter submodule number: ")
        if choice == 'q':
            os.chdir("..\\..\\..")
            moduleChoice()
        #File is now equal to the name of the chosen module
        file = os.listdir()[int(choice[0:2])-1]
        with open(file, 'r', encoding="utf8") as f:
            #Parses yaml file and puts it into a dictionary
            submoduleInfo = yaml.load(f, Loader=yaml.FullLoader)
        if "--id" in choice:
            print(f"ID: {submoduleInfo['id']}")
        if "--authors" in choice:
            for author in submoduleInfo["metadata"]["authors"]:
                print("Authors:")
                print(f"\t{author}")
        if "--name" in choice:
            print(f"Name: {submoduleInfo['name']}")
        if "--desc" in choice:
            print(f"Name: {submoduleInfo['description']}")
        if "--platforms" in choice:
            for platform in submoduleInfo["platforms"]:
                print("Platforms:")
                print(f"\t{platform}")
        if "--command" in choice:
            for platform in submoduleInfo["platforms"]:
                print("Commands:")
                for payload in submoduleInfo['platforms'][osInfo]:
                    print(f"\t{payload}")
                    print(
                        f"\t\t{submoduleInfo['platforms'][osInfo][payload]['command']}")
        if "--save" in choice or len(choice) <= 2:
            #True if the number of paylods is greater than 1
            if len(submoduleInfo['platforms'][osInfo]) > 1:
                #Then prints out all the vectors (cmd, pwh, etc)
                for payload in submoduleInfo['platforms'][osInfo]:
                    print(payload)
                choice = input("Enter command payload: ")
            else:
                choice = list(submoduleInfo['platforms'][osInfo])[0]
        if choice != "psh" and "--" not in choice:
            os.system(submoduleInfo['platforms'][osInfo][choice]["command"])
        elif choice == "psh" and "--" not in choice:
            command = submoduleInfo['platforms'][osInfo][choice]["command"].replace(
                "\n", "^")
            command = command.replace("%", "^%")
            command = command.replace("|", "^|")
            command = command.replace("&", "^&")
            command = command.replace("<", "^<")
            command = command.replace(">", "^>")
            command = command.replace('"', "'")
            command = command.replace('$HOME', expanduser("~"))
            print(command)
            os.system(f"powershell {command}")


def main():
    setup()
    colors.cprint(colors.GREEN, "OS detected: ", end='')
    print(osInfo.title())
    moduleChoice()


if __name__ == "__main__":
    main()
