from flask import Flask, render_template, request, redirect
import pandas as pd
import requests, io, os
import base64
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import HoverTool
from bokeh.charts import Scatter




app = Flask(__name__)

def get_stock(ticker):
    ticker = ticker
    apicall = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.csv?column_index=4&start_date=2012-11-01&end_date=2013-11-30'
    apikey = '&api_key=yRdMoLRR-tk-oNmDdQpd'
    strcall = apicall + apikey

    response = requests.get(strcall)
    df = pd.read_csv(io.BytesIO(response.content), delimiter = ',', sep = "\n")
    df['Date'] = pd.to_datetime(df['Date'])

    return df


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
    df['Date'] = pd.to_datetime(df['Date'])

    #source = ColumnDataSource(df)
    fig = figure(x_axis_type="datetime", title="Data from Quandle WIKI set")
    fig.line(df['Date'], df['Close'], color='#33A02C')
    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    html = render_template(
        'home.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)



if __name__ == '__main__':
  app.run(port=33507)
