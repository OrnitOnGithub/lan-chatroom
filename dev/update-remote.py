import version  # Now this should work
import os

version_num = str(int(version.fetch_remote_version()) + 1)

print(f"New version number: {version_num}")

version_file = "static/version.txt"

with open(version_file, "w") as file:
    file.write(str(version_num))

commit_msg = input("Enter commit message")

os.system("git add .")
os.system(f'git commit -m "{commit_msg}"')
os.system("git push")