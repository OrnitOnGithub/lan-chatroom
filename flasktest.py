from flask import Flask, render_template, request
import network as net
import webbrowser
import threading
import time
import sys
import os

auto_open_browser = True
browser = "safari"
msg_path = "public/messages.txt"
username_path = "username.txt"
with open(username_path, "r") as file:
    username = file.read()

def main():
    """
    with open(msg_path, "a") as file:
        file.write("\n" + username + " Joined the Chat")
    net.send()
    while True:
        msg = input()
        with open(msg_path, "a") as file:
            file.write("\n" + username + " : " + msg)
        net.send() # Sync
    """
    pass

def sendmsg(msg):
    with open(msg_path, "a") as file:
        file.write("\n" + username + " : " + msg)
    net.send() # Sync

def listen():
    net.listen()

app = Flask(__name__)

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
    time.sleep(0.3) # Lazy fix to stop race condition
    with open(msg_path, 'r') as file:
        file_content = file.read()
    return render_template('index.html', file_content=file_content)

@app.route('/refresh_text')
def refresh_text():
    with open(msg_path, 'r') as file:
        file_content = file.read()
    return render_template('chat.html', file_content=file_content)

if __name__ == '__main__':
    try:
        listen_thread = threading.Thread(target=listen)
        listen_thread.start()

        main_thread = threading.Thread(target=main)
        main_thread.start()

        if auto_open_browser:
            webbrowser.get(default_browser).open('http://127.0.0.1:5000')

        # Run the Flask app in a separate thread
        flask_thread = threading.Thread(target=app.run, kwargs={'debug': True, 'use_reloader': False, 'threaded': True})
        flask_thread.start()

        listen_thread.join()
        main_thread.join()
        flask_thread.join()

    except KeyboardInterrupt: # Ctrl+C
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)