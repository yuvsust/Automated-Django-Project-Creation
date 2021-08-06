import os 
import sys
import pathlib
import shutil

project_name = sys.argv[1]

# Fetch the current Directory path and replace '\' with '//'
current_dir = str(os.getcwd())
current_dir = current_dir.replace("\\", "//")

# Create a virtual environment, active it, install django, start a django project with the given 
# project name and then deactivate it
os.system("virtualenv venv")
os.chdir(current_dir + "//venv//Scripts")
os.system("activate")
print(" Installing Django ........")
os.system("pip install django")
print(" Initiating Django Project ........")
os.chdir(current_dir)
resp = os.system('django-admin startproject ' + project_name)

if resp == 0:
    os.chdir(current_dir)

    # Now move the venv folder to the project folder
    project_dir = current_dir + "//" + project_name
    venv_dir = current_dir + "//venv"
    shutil.move(venv_dir, project_dir + "//venv")

    # Now rename the project directory with a additional '-Project' string for coolness
    print(" Done\n Renaming the Parent Folder ........\n Done")
    os.rename(project_name, project_name+"-Project")
