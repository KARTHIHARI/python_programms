from pymongo import MongoClient
from flask import Flask,request
from bson.objectid import ObjectId


app=Flask(__name__)


def dbcon():
        conn=MongoClient("mongodb+srv://karthi:xeyCQSXq5JzNE2nl@myfirstdb.vf2qpzk.mongodb.net/")
        db=conn["SchoolProject"]
        col= db["Student"]      # data={"name" : "karthi","age":27}
        return col


#SHOW ALL QUERIES
@app.route("/students",methods=["GET"])
def table():
    try:
        col=dbcon()
        res=col.find()
        l=[]
        for data in res:
            l.append(data)
        return f"{l}"
    except Exception as e:
        print(str(e))
        return "Error",400
    

#SHOW QUERIES BASED ON NAME
@app.route("/students/<a>",methods=["GET"])
def name(a):
    try:
        col=dbcon()
        res=col.find({"name":a})
        l=[]
        for data in res:
            l.append(data)
        return f"{l}"
    except Exception as e:
        print(str(e))
        return "Error",400  
    

#SHOW QUERIES BTWN AGE
@app.route("/students/<int:a>/<int:b>",methods=["GET"])
def age(a,b):
    try:
        col=dbcon()
        res=col.find({"age":{ "$gte" :a, "$lte" :b}})
        l=[]
        for data in res:
            l.append(data)
        return f"{l}"
    except Exception as e:
        print(str(e))
        return "Error",400  


#INSERT DOCUMENT
@app.route("/students",methods=["POST"])
def insert():
    try:
        name= request.form["name"]
        age= request.form["age"]
        col=dbcon()
        data={"name" : name,"age":int(age)}
        res=col.insert_one(data)
        return "INSERTED"
    except Exception as e:
        print(str(e))
        return "Error",400
    

#UPDATE AGE BASED ON NAME
@app.route("/students",methods=["PUT"])
def updateage():
    try:
        id=request.form["id"]
        age= request.form["age"]
        name= request.form["name"]
        col=dbcon()
        res=col.update_one({'_id': ObjectId(id)},{"$set" :{"age":int(age),"name":name}})
        return "UPDATED"
    except Exception as e:
        print(str(e))
        return "Error",400
    



#DELETE QUERY BASED ON NAME
@app.route("/students/<a>",methods=["DELETE"])
def deletename(a):
    try:
        col=dbcon()
        res=col.delete_one({"name": a})
        return "DELETED"
    except Exception as e:
        print(str(e))
        return "Error",400  
    
#DELETE QUERY BASED ON AGE
@app.route("/students/<int:a>",methods=["DELETE"])
def deleteage(a):
    try:
        col=dbcon()
        res=col.delete_one({"age": int(a)})
        return "DELETED"
    except Exception as e:
        print(str(e))
        return "Error",400
 
    
app.run(debug=True,host="0.0.0.0")
