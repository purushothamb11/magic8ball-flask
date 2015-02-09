#!flask/bin/python
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    responses = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don\'t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful'];
    return '<h1> Hello from Github2:' + random.choice(responses) + '</h1>'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000) #debug=True)
