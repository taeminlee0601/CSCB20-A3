from flask import Flask

app = Flask(__name__)

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