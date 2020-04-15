# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:30:54 2020

@author: Rahul
"""
import json
import flask
from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
#import pandas as pd
#from flask_cors import CORS
from azure.storage.table import TableService

app = Flask(__name__)

app.config["DEBUG"] = False
#CORS(app)


@app.route("/")
def index():
    return render_template("test.html")


@app.route('/azpost/', methods=['POST'])
def post_data():

        result = json.dumps(request.form)
        result2 = json.loads(result)
        data_send = connection(result2, "", "insert")
        if data_send == "added Successfully!!!!":
            # flash('added Successfully!!!!')
            print(data_send)
            render_template("test.html")
            return str(data_send)
        else:
            return str(data_send)


'''@app.route('/azget/', methods=['post'])
def get_data():

        keys = request.form["keyname"]
        keys_value = request.form["keyval"]
        print(keys, keys_value)
        query = keys + " eq " + "'" + keys_value + "'"
        print(query)
        data_send = connection("", query, "reterive")
        return data_send
'''


acc_name = 'cloudshell1751970259'
acc_key = 'fufUNG+t4KF/qxAa4l1jObCovRMrvM4p/YO5M0jLyTK2x0L9njQLESukydU151dvIk0VVDL9xqIvTZuRPZ/D3g=='


def connection(tasks, query, types):
    table_service = TableService(account_name=acc_name, account_key=acc_key)
    table_service.create_table('customer')
    if types == "insert":
        print(tasks)
        table_service.insert_entity('customer', tasks)
        return "added Successfully!!!!"
    elif types == "reterive":
        # print(query)
        tasks = table_service.query_entities('customer', filter=query)
        # print(tasks)
       # df = pd.DataFrame(df_con(tasks))
        #data1 = df.to_json(orient='records')
        # print(data1)
        return "data1"


def df_con(tasks):
    for task in tasks:
        yield task


app.run()
