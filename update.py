import os

# Make a backup of your dada
os.system("cp config/* configbackup/")
# Fetch updates
os.system("git reset --hard")
os.system("git pull")
# Retrieve that backup
os.system("mv configbackup/* config/")