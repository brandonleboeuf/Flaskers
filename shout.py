from flask import Flask

app = Flask(__name__)

meaning_of_the_universe = 43

@app.route("/")
def hello_world():
    return f'<p>We\'re gonna learn the {meaning_of_the_universe}!</p>'
