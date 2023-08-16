# #flask
# from flask import Flask,request
# app=Flask(__name__)

# @app.route("/tri/<int:a>")
def tri(a):
    for i in range(a):
        for j in range(a):
            s="*"*a+"\n"
            s+=s
        return s
k=int(input())
print(tri(k))




# app.run(debug=True,host="0.0.0.0")