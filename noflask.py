import network as net
import threading
import time
import sys
import os

msg_path = "public/messages.txt"

username_path = "username.txt"
with open(username_path, "r") as file:
    username = file.read()


def main():

    with open(msg_path, "a") as file:
        file.write("\n" + username + " Joined the Chat")
    net.send()

    while True:
        msg = input()

        with open(msg_path, "a") as file:
            file.write("\n" + username + " : " + msg)

        net.send() # Sync

def listen():
    # This will run separately from the game.
    listen_thread = threading.Thread(target=net.listen())

    listen_thread.start()

if __name__ == '__main__':
    try:
        listen_thread = threading.Thread(target=listen)
        listen_thread.start()
        main()
    except KeyboardInterrupt: # Ctrl+C
        print('\nChat closed.')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
