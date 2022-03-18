from flask import request, Flask
from flask.templating import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def song():
    new_toDisplay = escape(request.args.get('toDisplay', ''))
    # print(new_toDisplay)
    with open('song.txt', 'w') as f:
        f.write(new_toDisplay)
    return render_template("toDisplay.html", toDisplay=new_toDisplay)
