from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = '''
    <h1>Te amo Marti</hi1>
    '''
    return html