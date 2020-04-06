from flask import Flask, render_template, request, redirect
import pandas as pd
import requests, io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    #return 'Hello World?'

@app.route('/about')
def about():
    #ticker = request.form['name_lulu']
    #return render_template('about.html', name = ticker)
    return render_template('about.html')

#Helper function
def get_plot(df):
    #Make plot and customize
    p = Scatter(df, x='Time', y='Prices',title='Stock Prices')
    p.title.text_font_size = '16pt'
    p.add_tools(HoverTool()) #Need to configure tooltips for a good HoverTool

    #Return the plot
    return(p)

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    ticker = request.form['name_ticker']
    print('This is another test')
    apicall = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/data.csv?column_index=4&start_date=2012-11-01&end_date=2013-11-30'
    apikey = '&api_key=yRdMoLRR-tk-oNmDdQpd'
    strcall = apicall + apikey



    response = requests.get(strcall)
    df = pd.read_csv(io.BytesIO(response.content), delimiter = ',', sep = "\n")
    #df.plot.line()
    shape = str(df.shape[0])

    #return shape

    #Setup plot
    p = get_plot(df)
    script, div = components(p)
    return render_template('about.html', script=script, div=div)
    #return render_template('index.html')


@app.route('/index_lulu', methods=['GET', 'POST'])
def index_lulu():
    return 'Hello Index_lulu'




if __name__ == '__main__':
  app.run(port=33507)
