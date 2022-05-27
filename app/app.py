from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objs as go

app = Dash(__name__)

def server_layout():
    df = pd.read_excel('/volumen/datos.xlsx')
    return html.Div([html.H1('piedras preciosas'),
                        html.Div('amo las piedras'),
                        html.Div(df['Articulo 1']),
                        html.Div(df['Articulo 2']),
                        html.Div(df['Articulo 3']),
                        html.Dib(df['Articulo 4']),])

app.layout = server_layout

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=80)
