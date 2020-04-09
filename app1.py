#column_datasource.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

import requests, io


output_file('columndatasource_example.html')

#ticker = request.form['name_ticker']
ticker = 'AAPL'
apicall = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.csv?column_index=4&start_date=2012-11-01&end_date=2013-11-30'
apikey = '&api_key=yRdMoLRR-tk-oNmDdQpd'
strcall = apicall + apikey

response = requests.get(strcall)
df = pd.read_csv(io.BytesIO(response.content), delimiter = ',', sep = "\n")
df['Date'] = pd.to_datetime(df['Date'])

print(df.head(4))

#source = ColumnDataSource(df)

p1 = figure(x_axis_type="datetime", title="Data from Quandle WIKI set")
# p1.grid.grid_line_alpha=0.3
# p1.xaxis.axis_label = 'Date'
# p1.yaxis.axis_label = 'Price'

p1.line(df['Date'], df['Close'], color='#33A02C', legend= ticker+':Close')
show(p1)
