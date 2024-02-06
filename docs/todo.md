# High-level TODO
- [x] Fix message getting reset issue
- [x] Make GUI
- [x] Make username.txt more restrictive
- [x] Ping to find users
  - [x] Display list of users
- [ ] Improve message synchronisation

## Pinging

How should we know who's online and who isn't?

### IDEA 1 (frankly, unnecessarily complicated)

Every `X` seconds, everyone broadcasts their username on the port.

every computer then appends that username to a list.

For each username, if it wasn't recieved in an timeframe arbitrarily larger than `X` seconds, that user can be considered offline.

EXAMPLE IN JSON
```json
[

    {
        "username" : "Ornit",
        "time_since_ping" : 9
    },
    {
        "username" : "Fortnite",
        "time_since_ping" : 4
    }
]
```

### IDEA 2 (most reasonable)

Pings. If someone recieves a ping, they will respond, notifying us of their presence.

## Message Synchronisation

### IDEA 1

Every message has an associated time to go with it. Then, every user iterates through every other user's message history and takes all messages, arranges them chronologically, removes duplicates and boom! A more accurate message history.

## Message reset issue

### IDEA 1

Just do GUI
- ~~Pygame (no)~~
- ~~Tkinter~~
- Web gooey
  - **Localhost web app (Flask)**
  - ~~Built-in web app (doesnt seem to work on school laptops though)~~