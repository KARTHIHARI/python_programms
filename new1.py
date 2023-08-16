from flask import Flask,request
import requests
import re
import json

import configparser

import smtplib
import ssl


app=Flask(__name__)
@app.route("/hello",methods=["POST","GET"])
def send_email(message:str):
    config = configparser.ConfigParser()

    config.read("config.ini")

    print(config["email"]["smtp"])
    print(config["email"]["user"])
    print(config["email"]["password"])

    SMTP_SERVER=config["email"]["smtp"]
    SMTP_USER=config["email"]["user"]
    SMTP_PASSWORD=config["email"]["password"]
    SENDER_EMAIL=config["email"]["user"]
    RECEIVER_EMAIL=["ammu@gmail.com","giridhaaran143@gmail.com"]
    for _ in range(3):
        try:
            context= ssl.create_default_context()
            with smtplib.SMTP_SSL(SMTP_SERVER,465, context=context) as server:
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
            print("mail sent!!!")
            return
        except Exception as exc:
            print("error!")
            print(exc)
    send_email("hello")
    l=send_email("hello")
    f=open("temp1.json","w")
    s=json.dumps(l,indent=4)
    f.write(s)
    return s
app.run(debug=True,host="0.0.0.0")
