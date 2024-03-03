from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/<input>')
def user(input):
    # Do not change name or it will change the url
    name = ''

    for i in range(len(input)):
        if input[i].isalpha():
            name += input[i]

    if name != input:
        return f"Welcome, {name}, to my CSCB20 Website"

    if name.strip() != name:
        f"Welcome, {name.strip()}, to my CSCB20 Website"
    
    if name.isupper():
        return f"Welcome, {name.lower()}, to my CSCB20 Website"
    
    if name.islower():
        return f"Welcome, {name.upper()}, to my CSCB20 Website"

    name = ''

    for i in range(len(input)):
        if (i == 0):
            name += input[i].upper()
        else:
            name += input[i].lower()

    return f"Welcome, {name}, to my CSCB20 Website"

if __name__ == '__main__':
    app.run()
=======
@app.route("/")
def home():
    return "Home"

@app.route("/<id>/")
def read(id):
    name = ""
    name += id
    name = name.strip()
    if not name.isalpha():
        new_name = ""
        for char in name:
            if char.isalpha():
                new_name += char
        return "Welcome, " + new_name + ", to my CSCB20 website!"
    if name.isupper():
        name = name.lower()
    elif name.islower():
        name = name.upper()
    else:
        if(len(name) > 0):
            name[0] = name[0].upper()
            if(len(name) > 1):
                name[1:] = name[1:].lower()
    return "Welcome, " + name + ", to my CSCB20 website!"

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> ec94992 (Bomin Q1)
