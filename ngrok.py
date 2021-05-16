import hashlib
from flask_ngrok import run_with_ngrok
from flask import Flask
users={}
class Register(object):
    def __init__(self,app):
        self.app=app
    def signup(self,username,password):
        hash=hashlib.md5(password.encode())
        users.update({username:hash.hexdigest()})
    def login(self,username,password):
        hash=hashlib.md5(password.encode())
        return users[username]==hash.hexdigest()
    
app=Flask(__name__)
u1=Register(app)
run_with_ngrok(app)
@app.route('/')
def home():
    return "hello all"
@app.route('/signup <username>,<password>')
def signup(username,password):
    u1.signup(username,password)
    return "updated successfully"
@app.route('/login <username>,<password>')
def login(username,password):
    if(u1.login(username,password)):
        return "login successfull {}".format(username)
    else:
        return "wrong credentials please check"
@app.route('/users')
def usersdata():
    return users
app.run()
