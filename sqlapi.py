from flask import Flask,request
from sqlalchemy import create_engine,text
import ssl


app=Flask(__name__)


def fun():
    ssl_context=ssl.create_default_context()
    ssl_context.verify_mode=ssl.CERT_REQUIRED
    connect_args={"ssl":ssl_context}
    # *
    sql_conn_str="mysql+pymysql://n6es7h5z3pnlzvh7giow:pscale_pw_6KGKQu916NbfBsFGGelsdo83AYqf6G5RM3GeMRb2d9d@aws.connect.psdb.cloud/first?ssl=true"
    #*
    engine=create_engine(sql_conn_str,connect_args=connect_args,)
    #*
    return engine.connect()


@app.route("/table",methods=["GET"])
def table():
    conn=fun()
    try :
    # a=request.args['name']
    # query=text("CREATE TABLE customersssgdvvjkbkjvhkv (name VARCHAR(255), email VARCHAR(255));")
    # query=text(f"select * from {a}")
        query=text("show tables")
        result=conn.execute(query)
        l=[]
        for data in result:
            data=" ".join(data)
            l.append(data)
            # return f"{data}"
    except:
        return "ERROR"
    finally:
        conn.close()
    return f"{l}"

@app.route("/col",methods=["GET"])
def col():
    conn=fun()
    a=request.args['name']
    try :
        # query=text("CREATE TABLE customersssgdvvjkbkjvhkv (name VARCHAR(255), email VARCHAR(255));")
        query=text(f"select * from {a}")
        # query=text("show tables")
        result=conn.execute(query)
        l=[]
        
        temp = ['id','name','email']
        
        for data in result:
            # j = 0
            # d={}
            l.append(data._mapping)
            # for i in data:
            #     d[temp[j]]=i
            #     j+=1
            # l.append(d)
            # l.append(data)
    except:
        return "ERROR"
    return f"{l}"

@app.route("/create",methods=["POST"])
def create():
    a=request.args['name']
    conn=fun()
    try:
        query=text(f"CREATE TABLE {a} (id int,name VARCHAR(255), email VARCHAR(255));")
        # query=text('show tables')
        result=conn.execute(query)
        l=[]
        for data in result:
           l.append(data)
    except:
        pass
    return f"{l}"

@app.route("/insert",methods=["POST"])
def insert():
    a=request.args["name"]
    b=request.args["id"]
    conn=fun()
    try:
        l=[]
        for i in range(1,int(b)+1):
            query=text(f"insert into {a} (id,name, email) values ({i},'haris','karthi@gmails')")
            result=conn.execute(query)
            for data in result:
                l.append(data)
    except:
            return "ERROR"
    return f"{l}"

@app.route("/",methods=["PUT"])
def update():
    a=request.args["name"]
    b=request.args["id"]
    conn=fun()
    try:
        query=text(f"update {a} set name='hariharasuthan' where id={b}")
        result=conn.execute(query)
        l=[]
        for data in result:
            l.append(data)
    except:
        return "ERROR"
    return f"{l}"

@app.route("/col",methods=["DELETE"])
def d():
    a=request.args["name"]
    b=request.args["id"]
    conn=fun()
    try:
        query=text(f"delete from {a} where id={b}")
        result=conn.execute(query)
        l=[]
        for data in result:
            l.append(data)
    except:
        return "ERROR"
    return f"{l}"

@app.route("/table",methods=["DELETE"])
def d2():
    a=request.args["name"]
    conn=fun()
    try:
        query=text(f"drop table {a}")
        result=conn.execute(query)
        l=[]
        for data in result:
            l.append(data)
    except:
        return "ERROR"
    return f"{l}"




app.run(debug=True,host="0.0.0.0")






    #username:password@host:port/database name  mysql default port no.3306
    # query=text("CREATE TABLE customers (name VARCHAR(255), email VARCHAR(255));")
    # query=text("insert into customers (name, email) values ('haris','karthi@gmails')")
    # query=text("update customers set name='harise' where email='karthi@gmail'")
    # query=text("delete from customers where name='haris'")