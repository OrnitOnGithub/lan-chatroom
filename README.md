# LAN Chatroom
This is a LAN chatroom made by your beloved Ornithopter747. It is made to be used in a completely decentralised way on a single network, allowing peer-to-peer schatting without any (external) servers.

## Table of contents:

- [LAN Chatroom](#lan-chatroom)
  - [Table of contents:](#table-of-contents)
- [**How to Use**:](#how-to-use)
  - [Download and Dependencies](#download-and-dependencies)
  - [Configuration](#configuration)
    - [Necessary config](#necessary-config)
    - [Extra config](#extra-config)
  - [Run it](#run-it)
  - [Updating](#updating)
  - [Technical Information](#technical-information)
  - [Plans for the Future](#plans-for-the-future)
  - [Want to Contribute?](#want-to-contribute)


# **How to Use**:

The setting up is a bit long. Sorry for the inconvenience, but I do recommend reading all of this document up until [Updating](#updating)

## Download and Dependencies
Download this repository by running:
```
git clone https://github.com/ornitongithub/lan-chatroom
```
in your terminal.

Open the folder you just downloaded/loned.

Install the dependencies
```
pip3 install -r requirements.txt
```
If that doesn't work, try:
```
pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org flask --user 
```
If this **STILL** doesn't work, make sure you're using python interpret 3.10+

## Configuration

There is a configuration file called `settings.json` that looks like this:
```json
{
    "username" : "YourUsernameHere",
    "port" : 12345,
    "open_browser" : true,
    "browser" : null,
    "colour" : "black"
}
```
This is where you can change different settings. To edit them, simpyl edit the field after the `:` like this:
```json
    "username" : "MyNewUsername",
    [...]
```

### Necessary config

`username` is obviously your username, what will be displayed to others using the chat.

`port` is the port you're chatting on. Think of this as a room. You only send and recieve messages from a certain port. Either use the default port `12345` or agree on a new port with your friends. (This number is always odd, as the following even port is used for other parts of the script (pinging users). If you set the port to an even number, it will be rounded up to the next odd number). <br>
Also, some ports are reserved for other activity by your computer. The free ports generally are `49152 - 65535`

`colour` is the colour your messages will appear in chat. Possible colours are:
- red
- orange
- yellow
- green
- blue
- purple
- black

### Extra config

Skip this part if you're not running into errors.

`open_browser` dictates wether the program will automatically open the browser for you (this is a web app). If you set it to false, you'll have to start your browser and visit `localhost:5000` yourself.

`browser` is the browser that gets open by default. `null` will open your default browser. If it doesn't work, or if you want to set the browser manually, change it like in these examples:
```json
    "browser" : "firefox",
```
```json
    "browser" : "safari",
```

## Run it

Run `main.py`. Either by running it in VSCode or by running
```
python3 main.py
```
in your terminal.

Normally a browser window should open automatically. If it does not, ckeck [Extra config](#extra-config)

Now that your browser opened the app, you can start chatting.

If your browser says "page not found" or anything along those lines, just try reloading the page.

To close the app, press `ctrl+c` in your terminal.

/!\ **WARNING:** You will only recieve and see messages that are sent while the script is running on your computer. (Technically there is nuance to this, but just remember not to trust the message history too much.)

## Updating

To update, run the update script:
```
python3 update.py
```

## Technical Information

This is a python web app that makes use of `Flask` and an old network library I wrote `network.py`.

For extra and more detailed information, check the `docs` directory.

## Plans for the Future

(NOTE: Everything is in `docs/todo.md`)

Features to add, in order:

In alpha:
- Finish UI 
  - DONE
- First release
  - DONE

In beta:
- Add list of active users
  - DONE
- Second release
  - DONE

We are here now (still in beta)

After release:
- Improve message synchronisation
- Final release

## Want to Contribute?

Please wait until the project's out of beta.