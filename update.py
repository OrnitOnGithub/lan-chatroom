import os

os.system("cp -r config configbackup")
os.system("git reset --hard")
os.system("git pull")
os.system("mv -r configbackup config")