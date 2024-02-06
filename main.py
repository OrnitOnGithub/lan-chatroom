from flask import Flask, render_template, request, make_response
from datetime import datetime
import network as net
import webbrowser
import threading
import time
import sys
import os

open_browser = True     # Wether the app will open your browser for you
browser = "safari"      # Which browser to open.
msg_path = "public/messages.txt"
username_path = "username.txt"
with open(username_path, "r") as file:
    first_line = file.readline()
    username = first_line[:20]
app = Flask(__name__)

user_list = []


def sendmsg(msg):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    with open(msg_path, "a") as file:
        file.write(f"\n[{current_time}] ({username}) {msg}")
    net.send() # Sync
    net.send() # net.send is unreliable, so run it twice because second time's the charm!

def update_user_list():
    global user_list
    # Start the receive_ping function in a separate thread
    ping_thread = threading.Thread(target=net.receive_ping)
    ping_thread.start()

    while True:
        user_list = [user['username'] for user in net.user_list] # Just a raw list of all users
        time.sleep(1)
        net.ping(username) # broadcast your username
        print(user_list)


def listen():
    net.listen()


@app.route('/')
def index():
    with open(msg_path, 'r') as file:
        file_content = file.read()
    return render_template('index.html', file_content=file_content)

@app.route('/add_text', methods=['POST'])
def add_text():
    text = request.form['text']
    print(f"Entered Text: {text}")  
    sendmsg(text)
    time.sleep(1) # Lazy fix to stop race condition
    with open(msg_path, 'r') as file:
        file_content = file.read()
    return render_template('index.html', file_content=file_content)

@app.route('/refresh_text')
def refresh_text():
    with open(msg_path, 'r') as file:
        file_content = file.read()
    return render_template('chat.html', file_content=file_content)

@app.route('/refresh_online_users')
def refresh_online_users():
    online_users = ' '.join(user_list)
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
        flask_thread = threading.Thread(target=app.run, kwargs={'debug': True, 'use_reloader': False, 'threaded': True})
        flask_thread.start()
        listen_thread.join()
        flask_thread.join()
        ping_thread.join()

    except KeyboardInterrupt: # Ctrl+C
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)