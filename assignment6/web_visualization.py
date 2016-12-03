import numpy as np
import matplotlib.pyplot as plt
from flask import Flask,render_template,request
app = Flask(__name__)

from temperature_C02_plotter import plot_temperature,plot_CO2,plot_co2_country

@app.route("/temperatur",methods=['GET','POST'])
def temperatur():
    import io
    import base64
     
    img = io.BytesIO()
   
    month = 'May'
    time_start = 1826
    time_end = 1900
    y_min = 0.0
    y_max = 30.0



    if(request.method == 'POST'):  
        month = request.form["month"]
        time_start = int(request.form["timeStart"])
        time_end = int(request.form["timeEnd"])
        y_min = float(request.form["yMin"])
        y_max = float(request.form["yMax"])

        
  
    plot_temperature("May",1816,1900,0,30)

    plt.savefig(img,format='png')
    img.seek(0)

    img64base = base64.b64encode(img.getvalue()).decode('ascii')

    return render_template('image.html',image = img64base) 


@app.route("/draw_temp",methods=['POST'])
def draw_temp():
    import io
    import base64
     
    # Acces the form data:
    month = request.form["month"]
    time_start = int(request.form["timeStart"])
    time_end = int(request.form["timeEnd"])
    y_min = float(request.form["yMin"])
    y_max = float(request.form["yMax"])
    # = request.form["password"]


    img = io.BytesIO()
        
    plot_temperature(month,time_start,time_end,y_min,y_max)

    plt.savefig(img,format='png')
    img.seek(0)

    img64base = base64.b64encode(img.getvalue()).decode('ascii')

    return render_template('image.html',image = img64base) 


@app.route("/CO2")
def co2():
    import io
    import base64
    
    img = io.BytesIO()
        
    plot_CO2(1816,1900,0,1000) 

    plt.savefig(img,format='png')
    img.seek(0)

    img64base = base64.b64encode(img.getvalue()).decode('ascii')

    return render_template('image.html',image = img64base) 

@app.route("/CO2_country")
def co2_country():
    import io
    import base64
    
    img = io.BytesIO()
        
    plot_co2_country(15.0,20.0)
    
    plt.savefig(img,format='png')
    img.seek(0)

    img64base = base64.b64encode(img.getvalue()).decode('ascii')

    return render_template('image.html',image = img64base) 



@app.route("/")
def home():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug = True)
    
