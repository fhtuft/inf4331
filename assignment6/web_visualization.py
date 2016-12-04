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

    return render_template('image_temp.html',image = img64base) 


@app.route("/CO2",methods=['GET','POST'])
def co2():
    import io
    import base64
    
    img = io.BytesIO()

    time_start = 1826
    time_end = 1900
    y_min = 0.0
    y_max = 30.0



    if(request.method == 'POST'):  
        time_start = int(request.form["timeStart"])
        time_end = int(request.form["timeEnd"])
        y_min = float(request.form["yMin"])
        y_max = float(request.form["yMax"])



        
    plot_CO2(time_start,time_end,y_min,y_max) 

    plt.savefig(img,format='png')
    img.seek(0)

    img64base = base64.b64encode(img.getvalue()).decode('ascii')

    return render_template('image_co2.html',image = img64base) 

@app.route("/CO2_country",methods = ['GET','POST'])
def co2_country():
    import io
    import base64
    
    img = io.BytesIO()
    
    min_co2 = 15.0
    max_co2 = 20.0
    

    if(request.method == 'POST'):  
        min_co2 = float(request.form["min_co2"])
        max_co2 = float(request.form["max_co2"])
    
        

    plot_co2_country(min_co2,max_co2)
    
    plt.savefig(img,format='png')
    img.seek(0)

    img64base = base64.b64encode(img.getvalue()).decode('ascii')

    return render_template('image_co2C.html',image = img64base) 

@app.route("/help")
def help_func():
    return render_template('temperature_C02_plotter.html')


@app.route("/")
def home():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug = True)
    
