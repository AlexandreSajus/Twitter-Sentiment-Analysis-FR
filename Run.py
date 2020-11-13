import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

from data_preprocessing import collectPolarity

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Input(id='my-input', value='Macron', type='text')
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input(component_id='my-input', component_property='value')])
def update_figure(value):

    fig = px.scatter(collectPolarity([str(value)]), x="date", y="polarity",color="opinion", color_discrete_sequence=['orange', 'green', 'red'])
    fig.update_layout()

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)