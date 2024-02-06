# Network

This is a pretty simple networking library that allows the synchronisation of data between two or more users.

This library does not use the standard client-server model. Instead, at any time either of the clients connected to the same port can send a packet that will synchronise a `public` directory with the one on the sender's computer.

For example one of the computers can make a change to `public/data.json` and can use `send()` to add those changes to the other computer(s).

# Usage

### The project must be organised like in this example:

```
public/
├─ data.anyformatyoulike
network.py
main.py
```

### In the main file, import network.

```python
import network as net
```

### The library provides two functions.

`send()` - This function will send all data in the `public` directory to all other computers connected to the same port (if they are listening)

`listen()` - This function listens for all incoming packets. It must run 100% of the time, and therefore must be run in a different thread from the main game loop. (as shown in the [example below](#example-usage))

# Example usage

```python
import network as net
import threading


def main():
    # Game logic goes here
    while True:
        # Let's say this adds changes to public/data.json
        DoSomething()
        # This will send all changes to all other connected clients
        net.send()
        

def network():
    # This will run separately from the game.
    # All this does is listen for incoming changes.
    # When there is a change, it will update the
    # public directory.

    # run net.listen() in a separate thread
    network_thread = threading.Thread(target=net.listen())
    network_thread.start()


if __name__ == "__main__":
    
    # Start the main() function as a separate thread
    main_thread = threading.Thread(target=main)
    main_thread.start()

    network()
```