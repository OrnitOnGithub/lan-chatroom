import threading
import time
import network as net

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

def network():
    # This will run separately from the game.
    network_thread = threading.Thread(target=net.listen())

    network_thread.start()



if __name__ == "__main__":
    main_thread = threading.Thread(target=network)
    main_thread.start()

    main()