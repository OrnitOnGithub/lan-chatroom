# LAN Chatroom

This is a LAN chatroom made by your beloved Ornithopter747. It is made to be used in a completely decentralised way on a single network, allowing encrypted peer-to-peer chatting without any (external) servers.

This software is no longer being updated frequently.

![](docs/lan-chatroom.png)

## Table of contents

- [LAN Chatroom](#lan-chatroom)
  - [Table of contents](#table-of-contents)
- [How to Use](#how-to-use)
  - [Download and Dependencies](#download-and-dependencies)
  - [Configuration](#configuration)
    - [The file contains the following fields:](#the-file-contains-the-following-fields)
  - [Extra configuration and info](#extra-configuration-and-info)
    - [Browsers](#browsers)
    - [Ports](#ports)
  - [Encryption](#encryption)
  - [Run it](#run-it)
  - [Updating](#updating)
  - [Plans for the Future](#plans-for-the-future)
  - [Want to Contribute?](#want-to-contribute)
  - [Want to Fork or use this code?](#want-to-fork-or-use-this-code)
- [New Features](#new-features)

# How to Use

## Download and Dependencies

Download this repository and open its containing folder by running the following command in your terminal.

```bash
git clone https://github.com/ornitongithub/lan-chatroom && cd lan-chatroom
```

The program will prompt you to install the dependencies when you [run it](#run-it). It will do so through pip. (If you want to install them yourself manually, they are in `requirements.txt`)

## Configuration

The configuration file is called `settings.json` and looks like this:

```json
{
  "username": "YourUsernameHere",
  "port": 12345,
  "colour": "black",
  "open_browser": true,
  "browser": null
}
```

### The file contains the following fields:

`username`: a legal username is between 3-20 characters, and contains no newline characters.

`port`: the port you're chatting on. Think of this as a room. You only send and recieve messages from a certain port. Either use the default port `12345` or agree on a new port with your friends.

`colour`: the colour your messages will appear. Possible colours are:

- <span style="color:red">red</span>
- <span style="color:orange">orange</span>
- <span style="color:gold">gold</span>
- <span style="color:green">green</span>
- <span style="color:blue">blue</span>
- <span style="color:purple">purple</span>
- <span style="color:black">black</span>

<br>

If you messed up or for any other reason want to reset, run:

```bash
git reset --hard
```

## Extra configuration and info

**Skip this part if you're not running into errors.**

### Browsers

`open_browser` dictates wether the program will automatically open the browser for you (this is a web app). If you set it to false, you'll have to start your browser and visit `localhost:5000` yourself.

`browser` is the browser that gets open by default. `null` will open your default browser. If it doesn't work, or if you want to set the browser manually, change it like in these examples:

```json
    "browser" : "firefox",
```

```json
    "browser" : "safari",
```

### Ports

By the way, the port number is always odd, as the following even port is used for other parts of the script (pinging users. If you set the port to an even number, it will be rounded up to the next odd number). <br>
If you were to use an even port, the program would just round it up to the next odd port. <br>
Also, some ports are reserved for other activity by your computer. The free ports generally are `49152 - 65535`. <br>
Keep in mind ports are not a security measure. Encyption is.

## Encryption

This program supports **symmetric** encryption. When sending a message, it gets encrypted with the encryption key. The default one is "default". It can be found in `key.txt`.

Any messages that cannot be decrypted (with your encryption key) will simply not be displayed. Make sure you and all your chatmates use the same key.

By the way, the key can be pretty much anything you can fit into that text file.

## Run it

Run `main.py`. Either by running `main.py` in VSCode or through the terminal:

```bash
python3 main.py
```

Make sure you're using python interpret 3.10+

Normally a browser window should open automatically. If it does not, ckeck [Extra config](#extra-config).

Now that your browser opened the app, you can start chatting.

If your browser says "page not found" or anything along those lines, just try reloading the page.

To close the app, press `ctrl+c` in your terminal.

## Updating

You can run the update script:

```bash
python3 update.py
```

This script updates and saves your config file. It however does not save key.txt.

## Plans for the Future

We are now in the final release. There are not so many plans anymore.
(NOTE: Everything is in `docs/todo.md`)

## Want to Contribute?

You can make a pull request. I will only accept *clean* bug fixes and small patches of the sort. No big features, sorry.

## Want to Fork or use this code?

Make sure you respect the `LICENSE` please. Thank you.

# New Features

Check [the release notes](Release-notes.md), thank you.
