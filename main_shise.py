from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/second')
def second():
    return render_template('second.html')


@app.route('/third')
def third():
    return render_template('third.html')


@app.route('/fourth')
def fourth():
    return render_template('fourth.html')


@app.route('/fifth')
def fifth():
    return render_template('fifth.html')


@app.route('/film')
def film():
    return render_template('film.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
