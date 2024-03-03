from flask import Flask

app = Flask(__name__)

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