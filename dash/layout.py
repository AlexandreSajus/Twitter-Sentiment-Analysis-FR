import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd

fig = px.scatter(pd.read_csv('./data_saved/scatter.csv'), x="polarity", y="subjectivity",color="opinion", color_discrete_sequence=['orange', 'green', 'red'])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H1('Sentiment Analysis Application'),
    html.Div(id='main-container', style={
            'height': '550px',
            'margin': '25px',
            'borderBottom': 'thin lightgrey solid'
        },
        children=[
        html.Div(id='input-container', style={
                'width': '35%',
                'height': '100%',
                'margin': '5px',
                'display': 'inline-flex',
                'background-color': '#eaeef0',
                'border-radius': '3px',
                'padding': '5px',
            }, children=[
            html.Ul(style={'list-style-type': 'none'},children=[
                html.Li([html.H3('Inputs')]),
                html.Li([
                    html.Div(id='search-container', style={'width': '400px'}, children=[
                        html.H4('Search'),

                        html.Label('Keywords and hastags :'),
                        dcc.Input(value='', id='search-input', type='text'),
                        
                        html.Label('Select mode'),
                        dcc.Dropdown(options=[
                            {'label': 'Positivity', 'value': 'positivity'},
                            {'label': 'Subjectivity', 'value': 'subjectivity'}
                        ], value='positivity', multi=True),
                        html.Button('Research', id='search-button'),
                        html.Div(id='output-search-button', style={'color': 'red', 'margin-top': '10px'},
                            children='No current research')
                    ])
                ]),
                html.Li([
                    html.Div(id='more-container', style={'width': '400px'}, children=[
                        html.H4('More...'),
                        dcc.Tabs(id='tabs-more', value='twitter', children=[
                            dcc.Tab(label='Twitter', value='twitter'),
                            dcc.Tab(label='Github', value='github'),
                        ]),
                        html.Div(id='tabs-content')
                    ])
                ]),
            ])
        ]),

        html.Div(id='result-container', style={
            'width': '61%',
            'height': '100%',
            'display': 'inline-flex',
            'background-color': '#eaeef0',
            'border-radius': '3px',
            'padding': '5px',
        }, children=[
            html.Ul(style={'list-style-type': 'none', 'white-space': 'nowrap'},children=[
                html.Li([html.H3('Graph')]),
                html.Li(children=[
                    html.Div(id='plot-container', style={'width': '700px'}, children=[
                        html.Label("Graph"),
                        dcc.Graph(id='plot',figure=fig),
                    ])
                ]),
                html.Li(children=[
                    html.Div(id='analysis-container', style={'width': '700px', 'float': 'right'}, children=[
                        html.Label('Analysis')
                    ])
                ]),
            ])
        ])
    ])
])

@app.callback(
    dash.dependencies.Output('output-search-button', 'children'),
    [dash.dependencies.Input('search-button', 'n_clicks')],
    [dash.dependencies.State('search-input', 'value')])
def update_output(n_clicks, value):
    return 'Current research : {}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)