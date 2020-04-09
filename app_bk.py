from flask import Flask, render_template, request, redirect
import pandas as pd
import requests, io, os
import base64
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import HoverTool
from bokeh.charts import Scatter




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    ticker = request.form['name_ticker']
    apicall = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.csv?column_index=4&start_date=2012-11-01&end_date=2013-11-30'
    apikey = '&api_key=yRdMoLRR-tk-oNmDdQpd'
    strcall = apicall + apikey

    response = requests.get(strcall)
    df = pd.read_csv(io.BytesIO(response.content), delimiter = ',', sep = "\n")
    #prices = (df.columns, df.shape)

    p = Scatter(df, x='sepal_length', y='sepal_width', title='Sepal width vs. length')
    p.title.text_font_size = '16pt'
    p.add_tools(HoverTool()) #Need to configure tooltips for a good HoverTool
    script, div = components(p)

    return render_template('home.html', script=script, div=div)




if __name__ == '__main__':
  app.run(port=33507)
