#column_datasource.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

import requests, io


output_file('columndatasource_example.html')

#ticker = request.form['name_ticker']
ticker = 'FB'
apicall = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.csv?column_index=4&start_date=2012-11-01&end_date=2013-11-30'
apikey = '&api_key=yRdMoLRR-tk-oNmDdQpd'
strcall = apicall + apikey

response = requests.get(strcall)
df = pd.read_csv(io.BytesIO(response.content), delimiter = ',', sep = "\n")


source = ColumnDataSource(df)

p = figure()
p.line(x='Date', y='Close',source=source)

hover = HoverTool()
hover.tooltips=[
    ('Attack Date', '@MSNDATE'),
    ('Attacking Aircraft', '@AC_ATTACKING'),
    ('Tons of Munitions', '@TOTAL_TONS'),
    ('Type of Aircraft', '@AIRCRAFT_NAME')
]

p.add_tools(hover)

show(p)
