from flask import Flask,request,render_template

app=Flask(__name__)

# @app.route("/",methods=["GET"])
# def fun():
#     return render_template("base.html",name="raj")
# app.run(debug=True,host="0.0.0.0")

# @app.route("/<name>",methods=["GET"])
# def fun(name):
#     return render_template("base.html",nme=name)
# app.run(debug=True,host="0.0.0.0")

# @app.route("/<name>",methods=["GET"])
# def fun(name):
#     return render_template("base.html",nme=name,colors=["red","blus","yellow"],d={"name":"this is hari"})
# app.run(debug=True,host="0.0.0.0")

from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/<int:n>",methods=["GET"])
def fact(n):
    # result={}
    l=[]
    f=1
    for i in range(n+1):
        if i==0:
            # result["0!"]=1
            l.append(1)
        else:
            f*=i
            # result[f"{i}!"]=f #(or)result[str(i)+"!"]
            l.append(f)
    return render_template("fact.html",relt=l)

app.run(debug=True,host="0.0.0.0")