from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/") #root, sort of home page
def hello():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        return f'Thanks for submitting the form {request.form["fname"]}!'
    return render_template('signup.html', signup=url_for('signup'))

@app.route('/Goodbye')
def goodbye():
    return "Goodbye, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)