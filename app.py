from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bug1')
def bug1():
    return render_template('bug1.html')


@app.route('/bug2')
def bug2():
    return render_template('bug2.html')


@app.route('/bug3')
def bug3():
    return render_template('bug3.html')


@app.route('/enhancement')
def enhancement():
    return render_template('enhancement.html')


@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/<arg1>/<arg2>/<arg3>/')
def arg3(arg1, arg2, arg3):
    return arg1 + " "  + arg2 + " " + arg3

if __name__ == '__main__':
    app.run()
