from flask import Flask
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']=True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
                }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>


    <!-- create your form here -->
        <form action="/webcaesar" methods='POST'>
        <label for="text">
        <input id="text" type="text" name="rot" value="0">
        </label>
        <p class="error">{rot_error}</p>
        <input type="textarea" name="text"><br>
        <input type="submit" value="Submit form">

        </form>
    </body>
    </html>
"""


def is_integer(rot):
    return True


@app.route("/webcaesar", methods=['POST'])
def encrypt(int):
    rot_enc= request.form['rot']
    text_enc = request.form['text']

    rot=''

    if not is_integer(rot):
        rot_error="Not a valid integer"
        rot_enc=''
    else:
        rot_enc=int(rot)

@app.route("/webcaesar", methods=['POST'])
def index():
    content = form + webcaesar
    return content

app.run()



