from json import load
from os import getcwd, walk, remove, makedirs
from os.path import abspath, join, exists, samefile
from shutil import copy, rmtree
from time import sleep
from urllib.request import urlretrieve
from zipfile import ZipFile

def getSettingsJSONOnStartup():
    with open("updaterSettings.cfg", "r") as f:
        return load(f)

try:
    print("StreamTicker update in progress. Please wait.")
    print("Loading updater settings")
    settings = getSettingsJSONOnStartup()
    print("Updater settings loaded")
    print("Downloading latest version...")
    urlretrieve(settings["downloadURL"], getcwd() + settings["temporaryZip"])
    print("Download complete. Unzipping...")
    with ZipFile(getcwd() + settings["temporaryZip"], 'r') as zip_ref:
        zip_ref.extractall(getcwd() + settings["temporaryExtractFolder"])
    print("Unzip complete. Calculating files to be updated...")

    root_src_dir = getcwd() + settings["temporaryExtractFolder"]
    root_dst_dir = settings["destinationDirectory"]

    fileCount = 0

    for src_dir, dirs, files in walk(root_src_dir):
        for file_ in files:
            fileCount += 1
    print("Updating " + str(fileCount) + " files")

    filesUpdated = 0
    for src_dir, dirs, files in walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not exists(dst_dir):
            makedirs(dst_dir)
            print("Added new folder: " + str(dst_dir))
        for file_ in files:
            filesUpdated += 1
            print("Updating file " + str(filesUpdated) + " of " + str(fileCount))
            src_file = join(src_dir, file_)
            dst_file = join(dst_dir, file_)
            if file_ in settings["doNotUpdateFiles"] and exists(dst_file):
                print("This file is in the updater's Do Not Update list and won't be updated: " + str(file_))
            else:
                if exists(dst_file):
                    if samefile(src_file, dst_file):
                        print("Same file found: " + str(file_))
                        continue
                    remove(dst_file)
                    print("Removed old file: " + str(file_))
                copy(src_file, dst_dir)
                print("Copied new file: " + str(file_))

    for dst_dir, dirs, files in walk(root_dst_dir):
        directory = abspath(dst_dir).replace(abspath(root_dst_dir), "").replace("\\", "", 1)
        if directory and any(directory.startswith(exclude) for exclude in settings["doNotCleanupDirectories"]):
            print("Skipping cleanup on directory: " + directory)
            continue
        src_dir = dst_dir.replace(root_dst_dir, root_src_dir, 1)
        if not exists(src_dir):
            rmtree(dst_dir)
            print("Cleanup detected an unknown folder and removed it: " + str(dst_dir))
            continue
        for file_ in files:
            src_file = join(src_dir, file_)
            dst_file = join(dst_dir, file_)
            if not exists(src_file) and not any(file_.endswith(extension) for extension in settings["doNotCleanupFileExtensions"]):
                remove(dst_file)
                print("Cleanup detected an unknown file and removed it: " + str(file_))

    remove(getcwd() + settings["temporaryZip"])
    rmtree(getcwd() + settings["temporaryExtractFolder"])
    print("The updater has finished. You may now close the window. This window will automatically close in 10 minutes.")
    sleep(600)
except Exception as e:
    print("The updater encountered an error and will now close.")
    print("Error information:")
    print(str(e))
    print("You may now close the window or copy this information for your records. This window will automatically close in 10 minutes.")
    sleep(600)

