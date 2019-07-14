#-*- coding: utf-8 -*-
__author__ = 'aditya'

from ts import app
from flask import render_template, request, make_response, jsonify, abort, redirect
import requests


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        request.files["resume"].read()
        post_data = request.form.to_dict()
        headers = {'content-type': 'application/json'}
        res = requests.post('http://127.0.0.1:5000/api/v1/application', json=post_data, headers=headers)
        print(res, "response")
        response = res.json()
        return render_template('index.html', response=response)


@app.errorhandler(400)
def page_not_found():
    return render_template("404.html"), 400


@app.route('/dashboard', methods=['GET'])
def dashboard():
    team_url = 'http://127.0.0.1:5000/api/v1/application'
    data = requests.get(url=team_url).json()['result']['applications']
    return render_template('dashboard.html', data=data)

