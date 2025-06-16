import random
from flask import Flask

app = Flask(__name__)
random_no = random.randint(0, 10)

@app.route("/")
def display():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:num>")
def guess(num):
    if num < random_no:
        return '<h1 style="color: red">Too low. Try Again!</h1>' \
            '<img src="//media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=400>'
    elif num > random_no:
        return '<h1 style="color: purple">Too high. Try Again!</h1>' \
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=400>'
    else:
        return '<h1 style="color: darkgreen">You found the number!! congrats!</h1>' \
            '<img src=" https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400>'


if __name__ == "__main__":
    app.run(debug=True)
