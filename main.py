from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

<form>
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
            <form method="post">
                <label for="rotate_by">Rotate by:</label>
                    <input type="text" name="rot" value ="0"/>
                    <textarea name="text" rows="5" cols="20"/>
                    <input type="submit"/>
            </form>
        </body>
    </html>
</form>

@app.route("/")
def index():
    return "Hello World"

app.run()