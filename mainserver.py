from random import choice, seed
from pandas import read_csv
from flask import Flask, request, jsonify, render_template, redirect, url_for
import Untitled

app = Flask(__name__)
 
@app.route('/')
def pickwinner():
    num = request.args.get('num')
    # num = int(num)
    winner = Untitled.pickandwin(num)
    return(winner)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug=True)