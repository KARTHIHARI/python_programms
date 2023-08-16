from flask import Flask,request
import math
app=Flask(__name__)

@app.route("/",methods=["GET","DELETE"])
def fun():
    print("args:",dict(request.args))
    if request.args["opt"]=="prime":
        x=int(request.args["value"])
        if x<3:
            return "True"
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return "False"
        return "True"
    elif request.args["opt"]=="fibbo":
        x=int(request.args["value"])
        l=[]
        a=0
        b=1
        for i in range(0,x):
            l.append(a)
            b=a+b
            a=b-a
        return l
    elif request.args["opt"]=="oe":
            x=int(request.args["value"])
            if x%2==0:
                return f"{x} is Even"
            else:
                return f"{x} is Odd"

app.run(debug=True,host="0.0.0.0")