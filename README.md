# OBS-Plugin: Text Display

This small script launches a webserver that accepts POST Requests and writes the contentent of the `toDisplay` key to a file ([`toDisplay.txt](./toDisplay.txt)). An OBS text field can be configered to display the content of this file.

## Installation
You need a python interpreter set up (Testet with 3.9.7). Than run: 

```PS
python.exe -m venv .venv
.\.venv\Script\activate
pip install requirements.txt
```

Than you need to create an OBS text field. Configure it to read the content to display from [`toDisplay.txt](./toDisplay.txt). You should now see a `Hello World`.

## Running
Run the server and enjoy:

```PS
flask run
```