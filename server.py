from flask import Flask, render_template

def login():
    pass



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

# TODO: respond to /login request.
@app.post('/login')
def login_post():
    return login()

# TODO: FLASK SESSIONS. https://flask.palletsprojects.com/en/2.2.x/quickstart/#sessions

app.run() # runs on local host. Go to 127.0.0.1
# app.run(host="0.0.0.0") to run on machine's IP address.