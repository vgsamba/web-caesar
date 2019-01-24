from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']=True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
                }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
             p.error {{
                color: red;
            }}
        </style>
    </head>

    <body>
        <!-- create your form here -->
        <form action="/" method="post">
            <label for="text"> Rotate by
            <input id="text" type="text" name="rot" value="0"> </input><br><br>
            </label>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
"""

@app.route('/', methods=['POST'])
def encrypt():
    rot_enc= int(request.form['rot'])
    text_enc = request.form['text']
    return form.format(rotate_string(text_enc,rot_enc))


@app.route("/")
def index():
    return form.format('')

app.run()



