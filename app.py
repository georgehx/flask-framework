from flask import Flask, render_template, request, redirect
import pandas as pd
import requests, io, os
import base64
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

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
    #return prices

    x = [1, 3, 5, 7]
    y = [2, 4, 6, 8]
    p = figure()

    p.line(x, y, color='blue', legend='line')
    #Setup plot

    script, div = components(p)

    #Render the page
    return render_template('about.html', script=script, div=div)

@app.route('/bokeh')
def bokeh():
    ticker = request.form['name_ticker']
    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    fig = figure(plot_width=600, plot_height=600)
    fig.vbar(
        x=[1, 2, 3, 4],
        width=0.5,
        bottom=0,
        top=[1.7, 2.2, 4.6, 3.9],
        color='navy'
    )

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    html = render_template(
        'about.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)





if __name__ == '__main__':
  app.run(port=33507)
