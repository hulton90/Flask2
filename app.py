from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpigbitch"


@app.route('/')
def index():  # put application's code here
    flash("What's your name?")
    return render_template('index.html')


@app.route('/greet', methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + "! Nice to meet you!")
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
