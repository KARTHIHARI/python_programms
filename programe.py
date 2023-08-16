from flask import Flask
import math

app=Flask(__name__)


@app.route("/prime/<int:x>")
def prime(x):
    if x<3:
        return "True"
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return "False"
    return "True"


@app.route("/fibbo/<int:x>")
def fibbo(x):
    l=[]
    a=0
    b=1
    for i in range(0,x):
        l.append(a)
        b=a+b
        a=b-a
    return l

@app.route("/oe/<int:x>")
def oe(x):
    if x%2==0:
        return f"{x} is Even"
    else:
        return f"{x} is Odd"

app.run(debug=True,host="0.0.0.0")

