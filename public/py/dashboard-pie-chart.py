import json

import js
import pandas as pd
import plotly
import plotly.express as px

## Get the data
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv"
url_content = open_url(url)

df = pd.read_csv(url_content)
df = df[df["Year"] == 2020]


def plot(chart):
    fig = px.pie(df, values="Month", width=400, height=300, hole=0.5)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    js.Plotly.newPlot("dashboard-pie-chart", js.JSON.parse(graphJSON))


plot("Tmax")
