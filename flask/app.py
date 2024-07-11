from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route('/eightball', methods=['GET','POST'])
def eightball():
    if request.method == 'POST':
        answers = ["I don't know", "/j", "hell no", "maybe", "no", "yeah, for sure"]
        return f'The eightball says {random.choice(answers)}!'
    return render_template('eightball.html', question=url_for('eightball'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)