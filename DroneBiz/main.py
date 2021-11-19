from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", title="home")


@app.route('/contact')
def contact():
    return render_template("contact.html", title="contact")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
