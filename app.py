#column_datasource.py
from flask import Flask, render_template, request
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
import requests, io

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

    #source = ColumnDataSource(df)

    #p1 = figure(x_axis_type="datetime", title="Data from Quandle WIKI set")
    # p1.grid.grid_line_alpha=0.3
    # p1.xaxis.axis_label = 'Date'
    # p1.yaxis.axis_label = 'Price'

    #p1.line(df['Date'], df['Close'], color='#33A02C', legend= ticker+':Close')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot():
#    ticker = request.form['name_ticker']
#@app2.route('/bokeh')
#def bokeh():
    ticker = request.form['name_ticker']
    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    df = get_stock(ticker)
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
    app.run(debug=True)
