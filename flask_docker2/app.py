from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    print("hello")
    return render_template('index.html')


app.run(debug=True, host='0.0.0.0', port=8888)