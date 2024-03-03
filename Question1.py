from flask import *

app = Flask(__name__)

@app.route('/<string:username>')
def welcome(username):
    username = username.strip()
    tmp = ''
    is_low = 0
    is_up = 0
    for i in range(len(username)):
        if username[i].isalpha():
            tmp += username[i]
            is_low |= username[i].islower()
            is_up |= username[i].isupper()
    username = tmp
    
    username = username.lower()
    if is_low and is_up:
        username = username[0].upper() + username[1:].lower()
    elif is_low:
        username = username.upper()
    return f'Welcome, {username}, to my CSCB20 Website'

if __name__ == "__main__":
    app.run(debug = True)