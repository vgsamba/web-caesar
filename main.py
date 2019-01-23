from flask import Flask, request
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
             p.error {
                color: red;
            }
        </style>
    </head>
    <body>


    <!-- create your form here -->
    <form action="/webcaesar" methods='POST'>
        <label for="text"> Rotate by
        <input id="text" type="text" name="rot" value="0"> </input><br><br>
        </label>
        <!-- <p class="error">{rot_error}</p>
        <input type="textarea" name="text" "rows="4" cols="50"> <br> <br>-->
        <textarea name="text" value="text"> </textarea>
        <input type="submit" value="Submit form">


    </form>
    </body>
</html>
"""



def is_integer(rot):
    return True


@app.route("/webcaesar", methods=['POST'])
def encrypt(text, rot):
    rot_enc= request.form['rot']
    text_enc = request.form['text']
    encrypted = ''
    for char in text_enc:
        encrypted = encrypted + rotate_string(char, rot_enc)
    return '<h1>{0}</h1>'.format(encrypted)

    """rot=''

    if not is_integer(rot):
        rot_error="Not a valid integer"
        rot_enc=''
    else:
        rot_enc=int(rot)"""


@app.route("/")
def index():

    return form

app.run()



