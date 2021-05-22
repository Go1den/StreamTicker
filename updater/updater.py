from json import load
from logging import info, basicConfig, INFO
from os import getcwd, walk, remove, makedirs, chdir
from os.path import abspath, join, exists, samefile
from shutil import copy, rmtree
from subprocess import Popen
from time import sleep
from urllib.request import urlretrieve
from zipfile import ZipFile

def getSettingsJSONOnStartup():
    with open("updaterSettings.cfg", "r") as f:
        return load(f)

def logAndPrint(s: str):
    info(s)
    print(s)

try:
    basicConfig(filename="log.txt", encoding="utf-8", level=INFO, format='%(asctime)s: %(message)s')
    logAndPrint("StreamTicker update in progress. Please wait.")
    logAndPrint("Loading updater settings")
    settings = getSettingsJSONOnStartup()
    logAndPrint("Updater settings loaded")
    logAndPrint("Downloading latest version...")
    urlretrieve(settings["downloadURL"], getcwd() + settings["temporaryZip"])
    logAndPrint("Download complete. Unzipping...")
    with ZipFile(getcwd() + settings["temporaryZip"], 'r') as zip_ref:
        zip_ref.extractall(getcwd() + settings["temporaryExtractFolder"])
    logAndPrint("Unzip complete. Calculating files to be updated...")

    root_src_dir = getcwd() + settings["temporaryExtractFolder"]
    root_dst_dir = settings["destinationDirectory"]

    fileCount = 0

    for src_dir, dirs, files in walk(root_src_dir):
        for file_ in files:
            fileCount += 1
    logAndPrint("Updating " + str(fileCount) + " files")

    filesUpdated = 0
    for src_dir, dirs, files in walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not exists(dst_dir):
            makedirs(dst_dir)
            logAndPrint("Added new folder: " + str(dst_dir))
        for file_ in files:
            filesUpdated += 1
            logAndPrint("Updating file " + str(filesUpdated) + " of " + str(fileCount))
            src_file = join(src_dir, file_)
            dst_file = join(dst_dir, file_)
            if file_ in settings["doNotUpdateFiles"] and exists(dst_file):
                logAndPrint("This file is in the updater's Do Not Update list and won't be updated: " + str(file_))
            else:
                if exists(dst_file):
                    if samefile(src_file, dst_file):
                        logAndPrint("Same file found: " + str(file_))
                        continue
                    remove(dst_file)
                    logAndPrint("Removed old file: " + str(file_))
                copy(src_file, dst_dir)
                logAndPrint("Copied new file: " + str(file_))

    for dst_dir, dirs, files in walk(root_dst_dir):
        directory = abspath(dst_dir).replace(abspath(root_dst_dir), "").replace("\\", "", 1)
        if directory and any(directory.startswith(exclude) for exclude in settings["doNotCleanupDirectories"]):
            logAndPrint("Skipping cleanup on directory: " + directory)
            continue
        src_dir = dst_dir.replace(root_dst_dir, root_src_dir, 1)
        if not exists(src_dir):
            rmtree(dst_dir)
            logAndPrint("Cleanup detected an unknown folder and removed it: " + str(dst_dir))
            continue
        for file_ in files:
            src_file = join(src_dir, file_)
            dst_file = join(dst_dir, file_)
            if not exists(src_file) and not any(file_.endswith(extension) for extension in settings["doNotCleanupFileExtensions"]):
                remove(dst_file)
                logAndPrint("Cleanup detected an unknown file and removed it: " + str(file_))

    remove(getcwd() + settings["temporaryZip"])
    rmtree(getcwd() + settings["temporaryExtractFolder"])
    logAndPrint("Update complete. Attempting to restart StreamTicker...")
    sleep(3)
    chdir(settings["destinationDirectory"])
    Popen(settings["restartExecutable"])
    exit(0)
except Exception as e:
    logAndPrint("The updater encountered an error and will now close.")
    logAndPrint("Error information:")
    logAndPrint(str(e))
    logAndPrint("You may need to manually download StreamTicker again to ensure all needed files are present.")
    logAndPrint("Information about this update failure was stored in streamticker/updater/log.txt. This window will automatically close in 10 minutes.")
    sleep(600)
    exit(1)
