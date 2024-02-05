# High-level TODO
- [ ] Ping to find users
- [ ] Display list of users

## Pinging

How should we know who's online and who isn't?

### IDEA 1

Every X seconds, everyone broadcasts their username on the port.

every computer then appends that username to a list.

For each username, if it wasn't recieved in an timeframe arbitrarily larger than X seconds, that user can be considered offline.

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