from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def whatName():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    print "Got Post Info"
    name = request.form['name']
    print request.form['name']
    return redirect('/')


app.run(debug=True)
