import os


versionfile = [os.path.join(root, x) for root, dirs, files in os.walk(os.getcwd()) for x in files if x == "version.py"]
