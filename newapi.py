from flask import Flask,request
app=Flask(__name__)

@app.route("/",methods=["GET","DELETE"])
def fun():
    print("METHOD :",request.method)
    return f"{dict(request.args)}"

@app.route("/",methods=["POST"])
def fun2():
    print("content:",request.content_type)
    return f"{dict(request.form)}"

app.run(debug=True,host="0.0.0.0")