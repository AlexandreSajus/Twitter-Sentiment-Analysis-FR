import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'style.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H1('Sentiment Analysis Application'),
    html.Div(className='main-container', children=[
        html.Div(className='input-container', children=[
            html.Ul([
                html.Li([html.H3('Inputs')]),
                html.Li([
                    html.Div(id='search-container', children=[
                        html.H4('Search'),

                        html.Label('Keywords and hastags :'),
                        dcc.Input(value='', type='text'),
                        
                        html.Label('Select mode'),
                        dcc.Dropdown(options=[
                            {'label': 'Positivity', 'value': 'positivity'},
                            {'label': 'Subjectivity', 'value': 'subjectivity'}
                        ], value='positivity', multi=True)
                    ])
                ]),
                html.Li([
                    html.Div(id='more-container', children=[
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

        html.Div(className='result-container', children=[
            html.Ul([
                html.Li([html.H3('Graph')]),
                html.Li([
                    html.Div(id='plot-container', children=[
                        html.Label("test") #html.H4('Graph'),dcc.Graph(id='plot',figure=fig),
                    ])
                ]),
                html.Li([
                    html.Div(id='analysis-container', children=[
                        html.H4('Analysis')
                    ])
                ]),
            ])
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)