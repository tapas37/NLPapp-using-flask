from flask import Flask,render_template,request,redirect# "render_template "->it load html files,"request"->to recieve data,"redirect"->for changeing to diffrent route
app=Flask(__name__)                            ## created a object of flask class
import api

from db import database
dbo=database()

@app.route('/')                                ## created a route--> can be think as URL-> jab koi apka url/website ka nam likh ke / marega ye function run hoga
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name=request.form.get("user's_name")
    email=request.form.get("user's_email")
    password=request.form.get("user's_password")
    response=dbo.insert(name, email, password)
    if response:
        return render_template('login.html',message="Registration Successful . Kindly login to proceed!")
    else:
        return render_template("register.html" ,message="Email already exists!")


@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get("user's_email")
    password = request.form.get("user's_password")
    response=dbo.search(email,password)
    if response:
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/ner')
def ner():
    return render_template('ner.html')


@app.route('/perform_ner',methods=['post'])
def perform_ner():
    text=request.form.get('ner_text')
    response=api.ner(text)
    print(response)
    formatted_response=[]
    for entity in response:
        formatted_response.append(f"Entity:{entity['entity']} | Category : {entity['category']}")


    return render_template('ner.html',response=formatted_response)


@app.route('/sa')
def sa():
    return render_template('sa.html')

@app.route('/perform_sa' , methods=["post"])
def perform_sa():
    text=request.form.get('sa_text')
    response=api.sentimetal_analysis(text)
    print(response)
    return render_template('sa.html',response=response)








app.run(debug=True)                            # (debug=True)->bar bar reload karne ki jaroorat nahi hai bas site pe jake reload karo
