from enyoencryption import encrypt, decrypt
from datetime import datetime
import socket
import json
import time

messages = ""
test_phrase = "The quick brown fox jumps over the lazy dog"

with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)
    username = settings["username"]
    open_browser = settings["open_browser"]
    browser = settings["browser"]
    colour = settings["colour"]
    # Assign a colour prefix to the user's chosen colour.
    # Note that editing the below dictionary might make
    # your message invalid.
    colourlist = {
        "black" : "/D",
        "red" : "/R",
        "orange" : "/O",
        "yellow" : "/Y",
        "green" : "/G",
        "blue" : "/B",
        "purple" : "/P"
    }
    try:
        user_colour = colourlist[colour]
    except:
        user_colour = "/D" # default (black)
    PORT = settings["port"]
    if PORT % 2 == 0:
        PORT = PORT + 1 # Force the port to be odd.
    PING_PORT = PORT+1
user_list = []  # Holds the list of online users.
TIMEOUT = 5     # If a user does not respond after this amount of seconds
                # they are considered offline.
last_execution_time = time.time()

with open("key.txt") as file:
    key = file.read() # Extract the encryption key


def username_is_valid(username) -> bool:
    """
    Logic to check is the entered username is legal.
    Rules:
    - 3 to 20 chars min/max
    - no newlines
    """
    if (len(username) < 3) or (len(username) > 20):
        return False
    if "\n" in username:
        return False
    # Otherwise,
    return True


# PINGING 
def ping(username):
    """
    Broadcast your username (and consequently IP) on the pinging
    port for others to know you're online.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    client_socket.sendto(username.encode('utf-8'), ('<broadcast>', PING_PORT))

def receive_ping():
    """
    This function updates an object called `user_list` that holds:
    - username
    - time since last ping
    - ip adress

    If the time since last ping exceeds the maximum timeout time,
    the user is removed from the list, as they are now offline.
    (probably)

    This function is also used by `send()` to send messages to every IP through
    TCP. So hijacking either `ping()` or `recieve_ping()` will make
    the chatroom unusable for you.
    """
    global last_execution_time
    global user_list

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', PING_PORT))

    while True:
        data, addr = server_socket.recvfrom(1024)
        username = data.decode('utf-8')
        if not username_is_valid(username): # If username is invalid
            username = "Illegal Username"
        user_ip = addr[0]  # Extract the IP address from the 'addr' tuple

        user_found = False
        for user in user_list:
            if user['ip'] == user_ip:
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
    """
    Sends a message JSON package to all IPs found in `user_list`.
    """
    global user_colour
    global test_phrase
    global user_list
    global username
    global key
    # Iterate over all users in the user_list and send the message to each one
    for user in user_list:
        ip = user["ip"]
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, PORT))
            packet = {
                "username": username,
                "message": encrypt(message, key),
                "colour": user_colour,
                "time": datetime.now().strftime("%H:%M"),
                "test_phrase": encrypt(test_phrase, key)
            }
            packet_json = json.dumps(packet)
            client_socket.sendall(packet_json.encode())

            # Close the connection after sending the message
            client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()

        except Exception as e:
            print(f"Failed to send message to {ip}: {e}")

def listen():
    """
    listen() must run constantly on a separate
    thread, as it needs to listen at all times
    for incoming messages.

    This function accepts incoming connections
    and recieves a JSON object. It then checks
    the validity of the package by checking the
    following:
    - legal uername
    - legal colour prefix
    - correct encryption test phrase
    - no empty fields

    If all tests pass, the message is formatted,
    recieved and appended to the `messages` var.
    """
    global test_phrase
    global colourlist
    global messages
    global key

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,  1)
    server_socket.bind(('0.0.0.0', PORT))  # Bind to all available network interfaces
    server_socket.listen()  # Start listening for incoming connections
    while True:
        conn, _ = server_socket.accept()  # Accept a new connection
        while True:
            data = conn.recv(2048)  # Receive up to 2048 bytes of data. That's a lot of data!
            if not data:
                break  # No more data from peer, this is some sort of mistake, exit the loop
            
            # Now we need to handle the data recieved!
            data = data.decode('utf-8')
            data = json.loads(data)
            # This is the data recieved.
            username = data['username']
            colour = data['colour']
            time = data['time']
            message_content = data['message']
            recieved_test_phrase = data['test_phrase']
            # Now we must check for the validity of the message before letting it through
            # We need to check for validity of:
            # - username
            #   - between 3-20 characters, no newlines
            # - colour
            # - encryption test phrase
            valid = True # To be set to false if a test fails
            # Check if the decrypted test phrase matches ours.
            # If it does it means the encryption key is correct.
            if decrypt(recieved_test_phrase, key) != test_phrase:
                valid = False
            # If any of the fields are empty, message is invalid.
            for x in data:
                if not data[x]:
                    valid = False
            # If the username is invalid, censor it.
            if not username_is_valid(username):
                username = "Illegal Username"
            # Check if the user sent a valid colour. Yes these are hardcoded sorry.
            if not colour in ["/D", "/R", "/O", "/Y", "/G", "/B", "/P"]:
                valid = False
            # Finally, add the approved message to the messages variable.
            if valid:
                messages += f"\n{colour}[{time}] ({username}) {decrypt(message_content, key)}"
        conn.close()  # Close connection after processing message.