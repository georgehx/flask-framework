from flask import Flask, render_template, request, redirect
import pandas as pd
import requests, io
import base64
from bokeh.plotting import figure

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
    print('This is another test')
    apicall = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.csv?column_index=4&start_date=2012-11-01&end_date=2013-11-30'
    apikey = '&api_key=yRdMoLRR-tk-oNmDdQpd'
    strcall = apicall + apikey

    response = requests.get(strcall)
    df = pd.read_csv(io.BytesIO(response.content), delimiter = ',', sep = "\n")
    #df.plot.line()
    shape = str(df.shape[0])
    prices = str(response.content)
    #return shape


    return prices


@app.route('/index_lulu', methods=['GET', 'POST'])
def index_lulu():
    return 'Hello Index_lulu'




if __name__ == '__main__':
  app.run(port=33507)
