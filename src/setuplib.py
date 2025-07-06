"""nv_templates installer library module. 

Version @release

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_templates
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from shutil import copytree
from shutil import copy2
import zipfile
import os
import sys
from pathlib import Path
try:
    from tkinter import *
except ModuleNotFoundError:
    print(
        (
            'The tkinter module is missing. '
            'Please install the tk support package for your python3 version.'
        )
    )
    sys.exit(1)

PLUGIN = 'nv_templates.py'
VERSION = ' @release'
SAMPLE_PATH = 'sample/'

root = Tk()
processInfo = Label(root, text='')
message = []

pyz = os.path.dirname(__file__)


def extract_file(sourceFile, targetDir):
    with zipfile.ZipFile(pyz) as z:
        z.extract(sourceFile, targetDir)


def extract_tree(sourceDir, targetDir):
    with zipfile.ZipFile(pyz) as z:
        for file in z.namelist():
            if file.startswith(f'{sourceDir}/'):
                z.extract(file, targetDir)


def cp_tree(sourceDir, targetDir):
    copytree(sourceDir, f'{targetDir}/{sourceDir}', dirs_exist_ok=True)


def extract_templates(templateDir):
    with zipfile.ZipFile(pyz) as z:
        for file in z.namelist():
            if file.startswith(SAMPLE_PATH):
                targetFile = file.replace(SAMPLE_PATH, '')
                if not targetFile:
                    continue
                if os.path.isfile(f'{templateDir}/{targetFile}'):
                    output(f'Overwriting "{templateDir}/{targetFile}" ...')
                else:
                    output(f'Copying "{templateDir}/{targetFile}" ...')
                with open(f'{templateDir}/{targetFile}', 'wb') as f:
                    f.write(z.read(file))


def cp_templates(templateDir):
    try:
        with os.scandir(SAMPLE_PATH) as files:
            for file in files:
                if os.path.isfile(f'{templateDir}/{file.name}'):
                    output(f'Overwriting "{templateDir}/{file.name}" ...')
                else:
                    output(f'Copying "{file.name}" ...')
                copy2(f'{SAMPLE_PATH}/{file.name}', f'{templateDir}/{file.name}')
    except:
        pass


def output(text):
    message.append(text)
    processInfo.config(text=('\n').join(message))


def main(zipped=True):
    if zipped:
        copy_file = extract_file
        copy_tree = extract_tree
        copy_templates = extract_templates
    else:
        copy_file = copy2
        copy_tree = cp_tree
        copy_templates = cp_templates

    scriptPath = os.path.abspath(sys.argv[0])
    scriptDir = os.path.dirname(scriptPath)
    os.chdir(scriptDir)

    # Open a tk window.
    root.title('Setup')
    output(f'*** Installing {PLUGIN}{VERSION} ***\n')
    header = Label(root, text='')
    header.pack(padx=5, pady=5)

    # Prepare the messaging area.
    processInfo.pack(padx=5, pady=5)

    # Install the plugin.
    homePath = str(Path.home()).replace('\\', '/')
    applicationDir = f'{homePath}/.novx'
    if os.path.isdir(applicationDir):
        pluginDir = f'{applicationDir}/plugin'
        os.makedirs(pluginDir, exist_ok=True)
        output(f'Copying "{PLUGIN}" ...')
        copy_file(PLUGIN, pluginDir)

        # Install the localization files.
        output('Copying locale ...')
        copy_tree('locale', applicationDir)

        # Install the sample templates.
        templateDir = f'{applicationDir}/templates'
        os.makedirs(templateDir, exist_ok=True)
        copy_templates(templateDir)

        # Show a success message.
        output(
            (
                f'Sucessfully installed "{PLUGIN}" '
                f'at "{os.path.normpath(pluginDir)}".'
            )
        )
    else:
        output(
            (
                'ERROR: Cannot find a novelibre installation '
                f'at "{os.path.normpath(applicationDir)}".'
            )
        )
    root.quitButton = Button(text="Quit", command=quit)
    root.quitButton.config(height=1, width=30)
    root.quitButton.pack(padx=5, pady=5)
    root.mainloop()
