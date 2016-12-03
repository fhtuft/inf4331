import numpy as np
import matplotlib.pyplot as plt
from flask import Flask,render_template
app = Flask(__name__)

from temperature_C02_plotter import plot_temperature,plot_CO2,plot_co2_country

@app.route("/temperatur")
def temperatur():
    import io
    import base64
     
    img = io.BytesIO()
        
    plot_temperature("May",1816,1900,0,30)

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
    
