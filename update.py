import os

# Yes I know this is dumb.

# Make a backup of your data
os.system("cp settings.json settingsbackup.json")
# Fetch updates
os.system("git reset --hard")
os.system("git pull")
# Retrieve that backup
os.system("mv settingsbackup.json settings.json")