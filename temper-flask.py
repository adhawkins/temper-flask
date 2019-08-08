#!/usr/bin/python3

from flask import Flask
from temper import Temper
from json import dumps

app = Flask(__name__)

@app.route('/')
def hello_world():
	temper = Temper()
	results = temper.read()
	return dumps(results)

if __name__ == '__main__':
	 app.run(host='::', debug=False)
