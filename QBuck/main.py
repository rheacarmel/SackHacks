from flask import Flask,render_template,request,jsonify
from flask_pymongo import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
# import sqlite3
app = Flask(__name__)

# url = 'mongodb+srv://vamsi:callodine25@cluster0.v3mwu.mongodb.net/test1?retryWrites=true&w=majority'
# mongo = pymongo.MongoClient(url)
# print(mongo.server_info())

@app.route("/")
def check():
    return render_template('index.html')

# @app.route("/get",methods=['GET'])
# def checkGet():
#     cur = mongo.db.names.find()
#     cur2 = dumps(cur)
#     print(cur2)
#     return jsonify(cur2)



@app.route('/post')
def show_post():
    # show the post with the given id, the id is an integer
    return request.args.get("user")

@app.route('/add',methods=['POST'])
def postCheck():
    # show the post with the given id, the id is an integer
    data = request.get_json()
    print(request.get_json())
    # mongo.db.test1.insert(data)
    return jsonify(data['name']),201

if __name__=="__main__":
    app.run(debug=True)
