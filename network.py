import zipfile
import socket
import json
import time
from datetime import datetime
import main # the main script so I can set some variables only there
import io
import os

messages = ""

test_phrase = "The quick brown fox jumps over the lazy dog"

with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)
    colour = settings["colour"]
    PORT = settings["port"]
    if PORT % 2 == 0:
        PORT = PORT + 1 # Force the port to be odd.
PING_PORT = PORT+1

user_list = []  # Holds the list of online users.
TIMEOUT = 5     # If a user does not respond after this amount of seconds
                # they are considered offline.
last_execution_time = time.time()


# PINGING 
def ping(username):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    client_socket.sendto(username.encode('utf-8'), ('<broadcast>', PING_PORT))

def receive_ping():
    global user_list, last_execution_time

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', PING_PORT))

    while True:
        data, addr = server_socket.recvfrom(1024)
        username = data.decode('utf-8')
        user_ip = addr[0]  # Extract the IP address from the 'addr' tuple

        user_found = False
        for user in user_list:
            if user['username'] == username:
                user['time_since_ping'] = TIMEOUT
                user_found = True
                break
        if not user_found:
            user_list.append({"username": username, "time_since_ping": TIMEOUT, "ip": user_ip})

        current_time = time.time()
        if current_time - last_execution_time >  1:
            last_execution_time = time.time()
            users_to_remove = []

            for user in user_list:
                user['time_since_ping'] -=  1
                if user['time_since_ping'] ==  0:
                    users_to_remove.append(user)

            for user in users_to_remove:
                user_list.remove(user)


def send(message):
    global colour
    global test_phrase, user_list  # Assuming 'test_phrase' and 'user_list' are defined globally
    username = main.username  # Fetch username from main script
    # Iterate over all users in the user_list and send the message to each one
    for user in user_list:
        ip = user["ip"]
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, PORT))
            packet = {
                "username": username,
                "message": message,
                "colour": colour,
                "time": datetime.now().strftime("%H:%M"),
                "test phrase": test_phrase
            }
            packet_json = json.dumps(packet)
            client_socket.sendall(packet_json.encode())

            # Close the connection after sending the message
            client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()

        except Exception as e:
            print(f"Failed to send message to {ip}: {e}")

def listen():
    global messages
    """
    listen() must run constantly on a separate
    thread, as it needs to listen all the time
    for changes to the public directory
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,  1)
    server_socket.bind(('0.0.0.0', PORT))  # Bind to all available network interfaces
    server_socket.listen()  # Start listening for incoming connections
    while True:
        conn, addr = server_socket.accept()  # Accept a new connection
        print(f"New connection from {addr}")
        while True:
            data = conn.recv(1024)  # Receive up to  1024 bytes of data
            if not data:
                break  # No more data from client, exit the loop
            # Now we need to handle the data recieved
            data = data.decode('utf-8')
            data = json.loads(data)
            messages += f"\n{data['colour']}[{data['time']}] ({data['username']}) {data['message']}"
            print(messages)
        conn.close()  # Close the connection after processing the message