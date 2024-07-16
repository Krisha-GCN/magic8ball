from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return render_template('homepage.html')

#ask.com

@app.route('/', methods=['GET','POST'])
def eightball():
    if request.method == 'POST':
        answers = ["I don't know", "/j", "hell no", "maybe", "no", "yeah, for sure"]
        return f"<h1> The eightball says {random.choice(answers)}! </h1>"
    return render_template('index.html', question=url_for('eightball'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=70, debug=True)

