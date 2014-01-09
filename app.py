# imports
from flask import Flask, render_template, request

# create app
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        return render_template('form.html',result=request.form['my_form'])
    if request.method == 'GET':
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug="true")
