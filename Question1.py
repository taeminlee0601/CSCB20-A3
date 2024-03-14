from flask import *

app = Flask(__name__)

@app.route('/<string:username>/')
def welcome(username):
    username = username.strip()
    tmp = ''
    is_low = 0
    is_up = 0
    for i in range(len(username)):
        if username[i].isalpha() and not username[i].isdigit():
            tmp += username[i]
            is_low |= username[i].islower()
            is_up |= username[i].isupper()
    
    if username == tmp:
        username = username.lower()
        if is_low and is_up:
            username = username[0].upper() + username[1:].lower()
        elif is_low:
            username = username.upper()
    else:
        username = tmp

    html_string = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Question 1</title>
    </head>
    <body>
        <h1>Welcome, {username} to my CSCB20 website!</h1>
    </body>
    </html>
    """

    return render_template_string(html_string)

if __name__ == "__main__":
    app.run(debug = True)