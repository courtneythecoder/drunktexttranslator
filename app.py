from flask import Flask, render_template
import random
app = Flask(__name__)

#TODO:varieties of drunkness ie wine, beer, tequila and vodka
#TODO:replace common autocorrects and random spelling errors
#TODO: Soberfier (Texticles 2.0) takes all drunk texts and turns them into
# compliments and nice quotes so no one knows you're drunk.
#TODO have the first time the submit button is hit erturn a message "sorry we
#out on the first date. Try again. "


@app.route('/')
def index():
    """
    WHATEVER I WANNA WRITE IS GONNA GO HERE. BITCHEDSSSS
    """
    return render_template("index.html")

@app.route("/texts")
def texts():
    textis = ["I'm not drinking tonight.", "Hey girl how are you tonight?", "Mom says I can't go out tonight"]
    text = random.choice(textis)
    return render_template("text.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
