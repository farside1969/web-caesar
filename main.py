from flask import Flask, render_template, redirect, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    empty_form = render_template("form.html")
    return empty_form

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    rotated_text = rotate_string(text, rot)
    return render_template('form.html',rotated_text = rotated_text)
    

app.run()