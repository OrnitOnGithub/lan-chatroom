# LAN Chatroom
This is a LAN chatroom made by your beloved Ornithopter747. It is made to be used in a completely decentralised way on a single network, allowing peer-to-peer schatting without any (external) servers.

## Table of contents:

- [LAN Chatroom](#lan-chatroom)
  - [Table of contents:](#table-of-contents)
- [**How to Use**:](#how-to-use)
  - [Updating](#updating)
  - [Technical Information](#technical-information)
  - [Plans for the Future](#plans-for-the-future)
  - [Want to Contribute?](#want-to-contribute)


# **How to Use**:
Download this repository by running:
```
git clone https://github.com/ornitongithub/lan-chatroom
```
in your terminal. You can also just click on `Code > Download zip` on GitHub if that's easier for you. However I'd recommend using git so that you can run the [update script](#updating)

Open the folder you just downloaded or cloned.

Set your username by editing `config/username.txt`. There is a 20 character limit and only the first line of the file is taken into account.

Install the dependencies
```
pip3 install -r requirements.txt
```
If that doesn't work, try:
```
pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org flask --user 
```
If this **STILL** doesn't work, make sure you're using python interpret 3.10+

If somehow it still still doesn't work, you can use the text-based version by running `noflask.py`. However this script is a last resort, it is outdated.

Run `main.py`. Either by running it in VSCode or by running
```
python3 main.py
```
in your terminal.

Normally a browser window should open automatically. If it does not, or you want to change which browser to open, edit these lines in `main.py`:
```python
open_browser = True     # Wether the app will open your browser for you
browser = None            # Which browser to open. None for default, "safari" for safari, etc.
```
This will be put in a configuration file later. Sorry for the inconvenience.

If you do not want the app to automatically open the browser for you, you must visit `localhost:5000` by yourself after starting `main.py`

Now that your browser opened the app, you can start chatting.

If your browser says "page not found" or anything along those lines, just try reloading the page. This is a pseudo race condition between the browser openning and the web app starting.

To close the app, press `ctrl+c` in your terminal.

If you want to change port, edit `config/port.txt`. Default is `12345`. <br>
This number is always odd, as the following even port is used for other parts of the script (pinging users). If you set the port to an even number, it will be rounded up to the next odd number. <br>
Also, some ports are reserved for other activity by your computer. The free ports normally are `49152 - 65535`

/!\ **WARNING:** You will only recieve and see messages that are sent while the script is running on your computer. (Technically there is nuance to this, but just remember not to trust the message history too much.)

/!\ **WARNING:** Both you and all recipients must be connected to the same network.

## Updating

To update, run the update script:
```
python3 update.py
```
This does require to have installed through git IIRC.

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