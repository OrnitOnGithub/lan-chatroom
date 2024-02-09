from flask import Flask, render_template, request
from datetime import datetime
import network as net
import webbrowser
import threading
import time
import json
import sys
import os

# Load the settings from the settings.json file
with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)

    username = settings["username"]
    open_browser = settings["open_browser"]
    browser = settings["browser"]



app = Flask(__name__)
user_list = []


def sendmsg(msg):
    net.send(msg)

def update_user_list():
    global user_list
    # Start the receive_ping function in a separate thread
    ping_thread = threading.Thread(target=net.receive_ping)
    ping_thread.start()

    while True:
        user_list = [user['username'] for user in net.user_list] # Just a raw list of all users
        time.sleep(1)
        net.ping(username) # broadcast your username


def listen():
    net.listen()


@app.route('/')
def index():
    return render_template('index.html', file_content=net.messages)

@app.route('/add_text', methods=['POST'])
def add_text():
    text = request.form['text'] 
    sendmsg(text)
    return render_template('index.html', file_content=net.messages)

@app.route('/refresh_text')
def refresh_text():
    return net.messages

@app.route('/refresh_online_users')
def refresh_online_users():
    online_users = '\n'.join(user_list)
    return online_users


if __name__ == '__main__':
    try:
        listen_thread = threading.Thread(target=listen)
        listen_thread.start()
        ping_thread = threading.Thread(target=update_user_list)
        ping_thread.start()

        if open_browser:
            webbrowser.get(browser).open('http://127.0.0.1:5000')

        # Run the Flask app in a separate thread
        flask_thread = threading.Thread(target=app.run, kwargs={'debug': False, 'use_reloader': False, 'threaded': True})
        flask_thread.start()
        listen_thread.join()
        flask_thread.join()
        ping_thread.join()

    except KeyboardInterrupt: # Ctrl+C
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)