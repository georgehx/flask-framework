from flask import Flask, render_template, request, redirect
import pandas as pd

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

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    ticker = request.form['name_ticker']
    print(ticker)
    apicall = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/data.csv?column_index=4&start_date=2012-11-01&end_date=2013-11-30'
    apikey = 'yRdMoLRR-tk-oNmDdQpd'
    strcall = apicall + apikey



    response = requests.get(strcall)
    df = pd.read_csv(response)
    df.plot.line()
    return render_template('index.html')

@app.route('/index_lulu', methods=['GET', 'POST'])
def index_lulu():
    return 'Hello Index_lulu'




if __name__ == '__main__':
  app.run(port=33507)
