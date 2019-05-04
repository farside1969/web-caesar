from flask import Flask, render_template, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_text = rotate_string(text, rot)
    return '<h1>' + encrypted_text + '</h1>'


app.run()