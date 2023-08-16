from flask import Flask,request
from sqlalchemy import create_engine,text
import ssl
import re


app=Flask(__name__)


def db_con():
    ssl_context=ssl.create_default_context()
    ssl_context.verify_mode=ssl.CERT_REQUIRED
    connect_args={"ssl":ssl_context}
    # *
    sql_conn_str="mysql+pymysql://n6es7h5z3pnlzvh7giow:pscale_pw_6KGKQu916NbfBsFGGelsdo83AYqf6G5RM3GeMRb2d9d@aws.connect.psdb.cloud/first?ssl=true"
    #*
    engine=create_engine(sql_conn_str,connect_args=connect_args,)
    #*
    return engine.connect()

@app.route("/students",methods=["POST"])
def add():
    roll_on=request.form["no"]
    name=request.form["name"]
    email=request.form["email"]
    if re.search(r'.+@gmail.com',email)==None:
         return "ENTER VALID INFORMATION"
    elif re.search(r'[0-9]',roll_on)==None:
         return {"ok":False,"msg":"ENTER VALID ROLL NUMBER"},400
    else:
        conn=db_con()
        try:
            # for i in range(1,int(b)+1):
            query=text("insert into STUDENTS (ROLLNO,NAME,EMAIL) values (:roll_on,:name,:email)")
            conn.execute(query, {'name':name, 'roll_on':roll_on, 'email':email})
        except Exception as e:
                return "error :"+str(e)
        return "DONE"

@app.route("/students",methods=["GET"])
def show():
    conn=db_con()
    try:
        query=text("select ROLLNO,NAME from STUDENTS")
        # query=text("show tables")
        result=conn.execute(query)
        l=[]
        
        temp = ['id','name','email']
        
        for data in result:
            # j = 0
            # d={}
            l.append(data._mapping)     #for modify to dict
            # for i in data:
            #     d[temp[j]]=i
            #     j+=1
            # l.append(d)
            # l.append(data)
    except Exception as e:
        return "ERROR:"+str(e)
    return f"{l}"

@app.route("/students/<int:a>",methods=["GET"])
def no(a):
    conn=db_con()
    try:
        query=text(f"select * from STUDENTS where ROLLNO='{a}'")
        # query=text("show tables")
        result=conn.execute(query)
        l=[]
        
        temp = ['id','name','email']
        
        for data in result:
            # j = 0
            # d={}
            l.append(data._mapping)     #for modify to dict
            # for i in data:
            #     d[temp[j]]=i
            #     j+=1
            # l.append(d)
            # l.append(data)
    except Exception as e:
        return "ERROR:"+str(e)
    return f"{l}"

@app.route("/students/<int:a>",methods=["DELETE"])
def no2(a):
    conn=db_con()
    try:
        # for i in range(1,int(b)+1):
        query=text(f"delete from STUDENTS where ROLLNO='{a}'")
        conn.execute(query)
    except Exception as e:
            return "error :"+str(e)
    return "DONE"


@app.route("/students/<int:a>",methods=["PUT"])
def modify(a):
    name=request.form["name"]
    email=request.form["email"]
    if re.search(r'.+@gmail.com',email)==None:
        return "ENTER VALID INFORMATION"
    else:
        conn=db_con()
        try:
            # for i in range(1,int(b)+1):
            query=text(f"update STUDENTS set NAME='{name}',EMAIL= '{email}' where ROLLNO='{a}'")
            conn.execute(query)
        except Exception as e:
                return "error :"+str(e)
        return "DONE"


app.run(debug=True,host="0.0.0.0")
