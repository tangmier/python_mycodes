#coding=utf-8
#在第一节课的基础上，增加用户注册的功能，并增加新用户登录功能
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from db import *    #将db.py导入

app = Flask(__name__)
from wtforms import Form, TextField, PasswordField, validators
class LoginForm(Form):
   username = TextField("username", [validators.required()])
   password = PasswordField("password", [validators.required()])

@app.route("/", methods=['GET','POST'])
def login():
    myForm = LoginForm(request.form)
    if request.method == 'POST':
        # if myForm.username.data == "jikexueyuan" and myForm.password.data == "123456" and myForm.validate():
        if (isExisted(myForm.username.data,myForm.password.data)):
            return redirect("http://www.jikexueyuan.com")
        else:
            message = "Login Failed"
        return render_template('index.html', message=message, form=myForm)
    return render_template('index.html', form=myForm)

@app.route("/register", methods=['GET', 'POST'])
def register():
    myForm = LoginForm(request.form)
    if request.method == 'POST':
        addUser(myForm.username.data, myForm.password.data)
        return "注册成功"
    return render_template('index.html', form=myForm)


if __name__ == "__main__":
    app.run(port=8080)
