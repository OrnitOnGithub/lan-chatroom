from flask import Flask, render_template, request
import dev.version as version
import network as net
import webbrowser
import threading
import time
import json
import sys
import os

# Load settings from settings.json file.
with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)

    username = settings["username"]
    open_browser = settings["open_browser"]
    browser = settings["browser"]

app = Flask(__name__) # God knows what this does
user_list = []        # List of online users, provided by net.user_list


def update_user_list():
    global user_list
    # Start the receive_ping function in a separate thread.
    ping_thr = threading.Thread(target=net.receive_ping)
    ping_thr.start()

    while True:
        user_list = [user['username'] for user in net.user_list] # Get list of all users
        time.sleep(1)
        net.ping(username) # broadcast your username


@app.route('/')
def index():
    return render_template('index.html', file_content=net.messages)

@app.route('/add_text', methods=['POST'])
def add_text():
    text = request.form['text'] 
    net.send(text)
    return render_template('index.html', file_content=net.messages)

@app.route('/refresh_text')
def refresh_text():
    return net.messages
# Maybe in the future refresh_text and refresh_online_users can be put together.
@app.route('/refresh_online_users')
def refresh_online_users():
    online_users = '\n'.join(user_list)
    return online_users

@app.route('/get_remote_version')
def get_remote_version():
    return version.fetch_remote_version()


if __name__ == '__main__':
    try:
        listen_thr = threading.Thread(target=net.listen)
        listen_thr.start()
        ping_thr = threading.Thread(target=update_user_list)
        ping_thr.start()

        if open_browser:
            webbrowser.get(browser).open('http://127.0.0.1:5000')

        # Run the Flask app in a separate thread
        flask_thr = threading.Thread(target=app.run,
                                     kwargs={'debug': False, 'use_reloader': False, 'threaded': True})
        flask_thr.start()
        listen_thr.join()
        flask_thr.join()
        ping_thr.join()

    except KeyboardInterrupt: # Ctrl+C
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)

    except Exception as e:
        print("\n"+e+"\n")