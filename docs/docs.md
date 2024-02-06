# General Documentation

## General structure of the project

### `public` directory

This folder holds all information that needs to be sent and synchronised across client.

`network.py` handles this folder.

Currently it only holds `messages.txt`, the history of previously sent messages.

### `templates` and `static` directories

templates: templates holds the html files to be rendered as our web app.

static: static holds the stylesheets for the html files.

### `.temp` directory

Used by `network.py`. Temporarily holds a zip file that is either recieved or to be sent.