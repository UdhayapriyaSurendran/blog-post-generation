from flask import Flask, request, render_template
from text_generation import generator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if request.method == "POST":
        rawtext = request.form['rawtext']
        max_words = request.form['max_words']
        generated_txt = generator(rawtext, int(max_words))

    return render_template('text_generation.html', generated_txt=generated_txt)


if __name__ == '__main__':
    app.run(debug=True)

