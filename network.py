import zipfile
import socket
import time
import io
import os
# I think all of this is already in the python standard library but fuck i know

port_path = "port.txt" # Default is 12345.
with open(port_path, "r") as file:
    PORT = int(file.read())
    if PORT % 2 == 0:
        PORT = PORT + 1 # Force the port to be odd.
PING_PORT = PORT+1

user_list = [] # Holds the list of online users.
TIMEOUT = 10    # If a user does not respond after this amount of seconds
                # they are considered offline.
last_execution_time = time.time()

def send():
    """
    send() synchronises the public directory with
    the other computer(s) connected to the port.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Folder to send
    folder_path = './public'
    archive_path = './.temp/folder.zip'  # Temporary ZIP file

    # Compress the folder into a ZIP file
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                archive.write(filepath, os.path.relpath(filepath, folder_path))

    # Send the ZIP file to the server
    with open(archive_path, 'rb') as file:
        # This should send it like everywhere i think
        client_socket.sendto(file.read(), ('<broadcast>', PORT))

# PINGING 
def ping(username):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    client_socket.sendto(username.encode('utf-8'), ('<broadcast>', PING_PORT))

def receive_ping():
    global user_list, last_execution_time  # Declare last_execution_time as global

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', PING_PORT))

    while True:
        data, addr = server_socket.recvfrom(1024)
        username = data.decode('utf-8')

        user_found = False
        for user in user_list:
            if user['username'] == username:
                user['time_since_ping'] = TIMEOUT
                user_found = True
                break  # Exit the loop if the user is found
        if not user_found:
            user_list.append({"username": username, "time_since_ping": TIMEOUT})

        current_time = time.time()
        if current_time - last_execution_time > 1: # If it's been more than one second
            last_execution_time = time.time()      # set time to actual time
            # Everything under this will be ran once every second.
            users_to_remove = []  # Create a list to store users to be removed

            for user in user_list:
                user['time_since_ping'] -= 1
                if user['time_since_ping'] == 0:
                    # print(f"{user['username']} is offline.")
                    users_to_remove.append(user)

            # Remove users after the iteration is complete
            for user in users_to_remove:
                user_list.remove(user)




def listen():
    """
    listen() must run constantly on a separate
    thread, as it needs to listen all the time
    for changes to the public directory
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', PORT))  # Bind to all available network interfaces

    while True:
        data, addr = server_socket.recvfrom(1024)  # 1 kb of data
        folder_zip = io.BytesIO(data)

        with zipfile.ZipFile(folder_zip, 'r') as archive:
            archive.extractall('./public')

