import time
import threading
import network  # Import the network module

def main():
    # Start the receive_ping function in a separate thread
    ping_thread = threading.Thread(target=network.receive_ping)
    ping_thread.start()

    # Your main script logic here
    while True:
        # Access user_list or perform other tasks using the module name as a prefix
        print(network.user_list)
        time.sleep(1)
        network.ping("username1")

if __name__ == "__main__":
    main() 