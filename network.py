import zipfile
import socket
import io
import os
import main
import flasktest
# I think all of this is already in the python standard library but fuck i know

PORT = 12345 # Default is 12345. use set_port() to change this.

def set_port(port):
    """
    Change the port used to communicate.
    Default is 12345.
    """
    global PORT
    PORT = port


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

        if data:
            flasktest.add_text()

        with zipfile.ZipFile(folder_zip, 'r') as archive:
            archive.extractall('./public')

        """
        # Shitty solution, but works idc
        print("")
        print("")
        print(f"Received and extracted folder from {addr}")
        print("===================")
        with open(main.msg_path, "r") as file:
            print(file.read())
        print("===================")
        print("Enter a msg: \n")
        """