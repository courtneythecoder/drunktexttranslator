from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route("/texts")
def texts():
    print
    textis = ["I'm not drinking tonight.", "Hey girl how are you tonight?", "Mom says I can't go out tonight"]
    text = random.choice(textis)
    return text

if __name__ == "__main__":
    app.run(debug=True)
