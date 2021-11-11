# IMPORT MODULES
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from datetime import datetime as dt
import subprocess
from apps import priv_pol, term_cond, feedback, auth, login
from app import app
from app import server
import requests
import urllib
import json

try:
    subprocess.run("lsof -t -i tcp:8080 | xargs kill -9", shell=False) # kill the server
except Exception as e:
    print(e)

profile = {}
userinfo = 'userinfo.json'
info = json.dumps(profile)
with open(userinfo, 'w') as f:
    f.write(info)

navbar = dbc.NavbarSimple(
    children=[

        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Support through Paypal", href="https://paypal.me/urbankizbook?country.x=NL&locale.x=nl_NL", target="_blank"),
                dbc.DropdownMenuItem("Buy a fully illustrated hardcover copy", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Support",
        ),
        dbc.NavItem(dbc.NavLink("Report a bug", href="#")),
        dbc.NavItem(dbc.NavLink("Logout", href="#")),
    ],
    brand="Feedback form - Urban kiz: a new vision on partner dance",
    brand_href="#",
    color="primary",
    dark=True,
    sticky=True,
)

app.layout = html.Div(children=[
                            navbar,
                            dcc.Location(id='url', refresh=False),
                            html.Div(id='page-content', children=[]),
                            dbc.Row([
                                    dcc.Link('Terms and conditions', href='/apps/term_cond'),
                                    dbc.Col('', width='1'),
                                    dcc.Link('Privacy policy', href='/apps/priv_pol')],
                            justify='center'),
                            ])
@app.callback(Output('page-content', 'children'),
              [Input('url', 'href')])
def display_page(href):
    if '/apps/priv_pol' in href:
        return priv_pol.layout
    elif '/apps/term_cond' in href:
        return term_cond.layout
    elif '/auth/google/callback' in href:
        print(href)
        url_dict = urllib.parse.parse_qs(href)
        code_item = next(iter(url_dict))
        code = url_dict[code_item][0]
        callback = login.AuthCallbackPage()
        callback.GET('google', code)
        return feedback.layout
    # elif "error" in pathname:
    #     print("Error logging in")
    #     return feedback.layout
    # elif "code" in pathname:
    #     print(pathname)
    #     print("Logging in succeeded")
    #     return feedback.layout
    else:
        return feedback.layout


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
