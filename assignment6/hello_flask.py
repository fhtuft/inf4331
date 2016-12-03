import numpy as np
import matplotlib.pyplot as plt

from flask import Flask,render_template
app = Flask(__name__)

users = {"richard": "Richard Lee",
         "john": "John Smith"}

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route("/user")
def show_user_overview():
    users_str = "<br>".join(users.values())
    return '<h1>Our users</h1><br>{}'.format(users_str)

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/handel_login',methods=['POST'])

def handel_login():

    assert request.methode == 'POST'

     # Acces the form data:
    username = request.form["username"]
    password = request.form["password"]
    

    if username == "simon" and password == "safe":                                      
        return "You are logged in Simon"
    else:
        error = "Invalid credentials"   
    
    return render_template("login.html", error=error)

def ploter():
    import io
    import base64
    
    t = np.linspace(0,10)
    u = np.linspace(0,10)
    
    img = io.BytesIO()
        
    plt.plot(t,u)

    plt.savefig(img,format='png')
    img.seek(0)

    img64base = base64.b64encode(img.getvalue())

    return img64base

@app.route("/image") 
def plot_image():

    import io
    import base64
    
    t = np.linspace(0,10)
    u = np.linspace(0,10)
    
    img = io.BytesIO()
        
    plt.plot(t,u)

    plt.savefig(img,format='png')
    img.seek(0)

    img64base = base64.b64encode(img.getvalue()).decode('ascii')

    return render_template('image.html',image = img64base) 


if __name__ == '__main__':

    #img64base = ploter()
    app.run(debug = True)

