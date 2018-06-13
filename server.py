from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
