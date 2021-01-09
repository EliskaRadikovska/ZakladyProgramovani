import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    html.Div([html.Label('Hello, what do you like to do in your free time?')], style={'display': 'inline-block', 'vertical-align': 'middle','textAlign': 'center', 'font-size': '1.6em', 'width':'40%'}),
    dcc.Dropdown(id='example-dropdown',options=[{'label': 'Read books', 'value': 'read'},{'label': 'Bake cakes', 'value': 'bake'},],value=''),
    dcc.Graph(id='example-plot',figure={'data': [go.Bar(x=[1], y=[628], name='Paperback'),go.Bar(x=[1], y=[796], name='Hard book')],'layout': {'title': 'Book weight in grams'}}),
    html.Div(id='display-text'),
    dcc.Input(id='bar1', type="text", value='10'),
    dcc.Input(id='bar2', type="text", value='20'),
    html.Button(id='submit-button', n_clicks=0, children='nastav graf')
])

@app.callback(
    Output(component_id='display-text', component_property='children'),
    Input(component_id='example-dropdown', component_property='value')
)
def update_output_div(input_value):
    return 'You selected "{}"'.format(input_value)

@app.callback(Output('example-plot', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('bar1', 'value'),
    State('bar2', 'value')])
def update_function(n_clicks, bar1, bar2):
    return {'data': [go.Bar(x=[1], y=[bar1], name='Paperback'),go.Bar(x=[1], y=[bar2], name='Hard book')],'layout': {'title': 'Book weight in grams'}}

app.run_server(debug=True)
