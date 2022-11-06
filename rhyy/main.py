from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = '''
    <h1>Rhyy</hi1>
    <h2>Test</h2>
    '''
    return 