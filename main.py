# IMPORT MODULES
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from datetime import datetime as dt
import subprocess
from apps import priv_pol, term_cond, feedback
from app import app
from app import server

try:
    subprocess.run("lsof -t -i tcp:8080 | xargs kill -9", shell=False) # kill the server
except Exception as e:
    print(e)


app.layout = html.Div(children=[
                            dcc.Location(id='url', refresh=False),
                            html.Div(id='page-content', children=[]),
                            dbc.Row([
                                    dcc.Link('Terms and conditions', href='/apps/term_cond'),
                                    dbc.Col('', width='1'),
                                    dcc.Link('Privacy policy', href='/apps/priv_pol')],
                            justify='center'),
                            ])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/priv_pol':
        return priv_pol.layout
    elif pathname == '/apps/term_cond':
        return term_cond.layout
    else:
        return feedback.layout



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
