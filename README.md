# LAN Chatroom
This is a LAN chatroom made by your beloved Ornithopter747.

Table of contents:

- [LAN Chatroom](#lan-chatroom)
  - [**How to Use**:](#how-to-use)
  - [Technical Information](#technical-information)
  - [Plans for the Future](#plans-for-the-future)
  - [Want to Contribute?](#want-to-contribute)


## **How to Use**:
There are no releases yet, so download this repository by running:
```
git clone https://github.com/ornitongithub/lan-chatroom
```
in your terminal. You can also just click on `Code > Download zip` on GitHub if that's easier for you.

Open the folder you just downloaded or cloned.

Set your username by editing `username.txt`

Install the dependencies
```
pip3 install -r requirements.txt
```

Run `main.py`. Either by running it in VSCode or by running
```
python3 main.py
```
in your terminal.

Normally a browser window should open automatically. If it does not, edit these lines in `main.py`:
```python
open_browser = True     # Wether the app will open your browser for you
browser = "safari"      # Which browser to open.
```
If you do not want the app to automatically open the browser for you, you must visit `localhost:5000` by yourself after starting `main.py`

Now that your browser opened the app, you can start chatting.

To close the app, press `ctrl+c` in your terminal.

/!\ **WARNING:** You will only recieve and see messages that are sent while the script is running on your computer.

/!\ **WARNING:** Both you and all recipients must be connected to the same network.

## Technical Information

This is a python web app that makes use of `Flask` and an old network library I wrote `network.py`.

For extra and more detailed information, check the `docs` directory.

## Plans for the Future

Features to add, in order:

In alpha:
- Finish UI
- First release

In beta:
- Add list of active users
- Second release

After release:
- Improve message synchronisation
- Final release

## Want to Contribute?

Please wait until the project's out of beta.