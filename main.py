# IMPORT MODULES
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import subprocess
from apps import priv_pol, term_cond, thanks, login # feedback app is imported in the callback because otherwise error due to to late loading of form
from app import app
from app import server
import urllib
import json
import flask
import dash
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import db, Feedback



# try:
#     subprocess.run("lsof -t -i tcp:8080 | xargs kill -9", shell=False) # kill the server
# except Exception as e:
#     print(e)


navbar = dbc.NavbarSimple(
    children=[

        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Support my writing through Paypal", href="https://paypal.me/urbankizbook?country.x=NL&locale.x=nl_NL", target="_blank"),
                dbc.DropdownMenuItem("Buy a fully illustrated hardcover copy", id="buy", n_clicks=0, href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Support",
        ),
        dbc.NavItem(dbc.NavLink("Report a bug", id='report-bug', href="#")),
        dbc.NavItem(dbc.NavLink("Logout", id="logout", href="/logout")),
    ],
    brand="Feedback form - Urban kiz: a new vision on partner dance",
    brand_href="/",
    color="primary",
    dark=True,
    sticky=True,
)


app.layout = html.Div(children=[
                            navbar,
                            dcc.Location(id='url', refresh=False),
                            html.Div(id="page-content", children=[
                            ]),
                            dbc.Row([
                                    dcc.Link('Terms and conditions', href='/apps/term_cond'),
                                    dbc.Col('', width='1'),
                                    dcc.Link('Privacy policy', href='/apps/priv_pol'),
                                    # dbc.Col('', width='1'),
                                    # dcc.Link("Logout", href="/logout"),
                            ],
                            justify='center'),
                            html.Br(),
                            html.Div(id='empyt-div',children=[]),
                            html.Div(id="hidden_div_for_redirect_callback", children=[]),
                            html.Div(id="hidden_div_for_redirect_callback2", children=[]),
                            dbc.Modal([
                                            dbc.ModalHeader("Report a bug"),
                                            dbc.ModalBody(children=(dcc.Textarea(
                                                id='textarea',
                                                value='',
                                                style={'width': '100%', 'height': 300},
                                            ),)
                                            ),
                                            dbc.ModalFooter(children=[
                                                dbc.Button("Send", id="send-email", className="ml-auto", n_clicks=0),
                                            ]
                                            ),
                                        ],
                                        is_open=False,
                                        id="modal-bug",
                                        style={"white-space": "break-spaces"},
                                        backdrop=True
                                    ),
                            dbc.Modal([
                                dbc.ModalHeader("Hardcover copy"),
                                dbc.ModalBody(children=(
                                    html.Div("Your name and e-mail adress have been registered. I will incorporate the feedback I get. You will receive a mail when the hardcover version is ready. "),
                                )
                                ),
                                dbc.ModalFooter(children=[
                                    dbc.Button("Close", id="close-hardcover", className="ml-auto", n_clicks=0),
                                ]
                                ),
                            ],
                                is_open=False,
                                id="modal-hardcover",
                                style={"white-space": "break-spaces"},
                                backdrop=True
                            ),
                            ])
@app.callback(Output('page-content', 'children'),
              [Input('url', 'href')])
def display_page(href):
    print("printing href")
    print(href)
    from apps import feedback
    # placed import feedback over here because otherwise the loading of the callback is going to be faster then
    # the layout loading, causing an error of input not found of callback
    allcookies = dict(flask.request.cookies)
    print("printing allcookies for displaying page")
    print(allcookies)
    if ("/thanks" in href) or allcookies.get('_close'):
        print(href)
        dash.callback_context.response.set_cookie('_close', "submitted_form")
        return thanks.layout
    elif '/apps/priv_pol' in href:
        return priv_pol.layout
    elif '/apps/term_cond' in href:
        return term_cond.layout
    elif '/auth/google/callback' in href:
        print(href)
        print("authenticated")
        url_dict = urllib.parse.parse_qs(href)
        code_item = next(iter(url_dict))
        code = url_dict[code_item][0]
        callback = login.AuthCallbackPage()
        callback.GET('google', code)
        return feedback.layout
    elif "/logout" in href:
        print(href)
        callback = login.LogoutPage()
        callback.GET()
        return feedback.layout
    else:
        return feedback.layout


global text_old
text_old = ""

@app.callback(
    Output("modal-bug", "is_open"),
    [Input("report-bug", "n_clicks"), Input("send-email", "n_clicks"), Input("textarea", "value")],
    [State("modal-bug", "is_open")],
)
def notes_modal(n1, n2, text, is_open):
    print("something")
    global text_old
    data = Feedback("a", "b", 1, 2,3,4, "c")
    db.session.add(data)
    db.session.commit()
    if text != text_old:
        allcookies = dict(flask.request.cookies)
        print(allcookies)
        try:
            d = allcookies['_profile']
            d = json.loads(d)
            name = d['name']
        except Exception as e:
            print(e)
            name = "Unknown"
        bug_file = 'bug.json'
        with open(bug_file, 'w') as f:
            f.write(str({name:text}) + "\n")
        text_old = text
        return is_open
    elif n2 or n1:
        return not is_open
    return is_open

@app.callback(
    Output("modal-hardcover", "is_open"),
    [Input("buy", "n_clicks"), Input("close-hardcover", "n_clicks")],
    [State("modal-hardcover", "is_open")],
)
def hardcover_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal", "is_open"),
    Output("modal2", "is_open"),
    Output("hidden_div_for_redirect_callback2", "children"),
    [Input("1", "value"),
     Input('2', 'value'),
     Input('3', 'value'),
     Input('4', 'value'),
     Input('5', 'value'),
     Input('6', 'value'),
     Input('7', 'value'),
     Input('textarea1', 'value'),
     Input('textarea2', 'value'),
     Input('textarea3', 'value'),
     Input('textarea4', 'value'),
     Input('textarea5', 'value'),
     Input('textarea6', 'value'),
     Input('textarea7', 'value'),
     Input('submit-button', 'n_clicks'),
     Input('save', 'n_clicks'),
     Input('close', 'n_clicks')],
    [State("modal", "is_open"),
     State("modal2", "is_open")],
)
def submit(Question1, Question2, Question3, Question4, Question5, Question6, Question7,text1, text2, text3, text4, text5, text6, text7, submitclick, save, close, is_open, is_open2):
    if save == 0 and submitclick== 1:
        return not is_open, is_open2, None
    elif submitclick >1:
        return is_open, not is_open2, None
    elif close:
        return not is_open, not is_open2, dcc.Location(href="/thanks",
                           id="someid")
    elif save == 1 and submitclick==1:
        print(Question1, Question2, Question3, Question4, Question5, text1, text2, text3, text4)
        return is_open, not is_open2, None
    return is_open, is_open2, None

@app.callback(
    Output("hidden_div_for_redirect_callback", "children"),
    Output("modal3", "is_open"),
    [Input('google-login', 'n_clicks'),
     Input('register-manual', 'n_clicks'),
     Input('name', 'value'),
     Input('email', 'value')],
    [State("modal3", "is_open")],
)
def google_manual_login(a,b, name, email, c,):
    print(a,b, name, email, c,)
    allcookies = dict(flask.request.cookies)
    print("these are the current cookies:", allcookies)
    if a==1 and b==0:
        auth = login.AuthPage()
        auth_url = auth.GET("google")

        return dcc.Location(href=auth_url,
                           id="someid"), False
    elif a==0 and b==1:
        dash.callback_context.response.set_cookie('_id', "register_manual")
        dash.callback_context.response.set_cookie('_profile', '{'+'"name"'+':"'+ str(name)+'"}')
        return "", False
    else:
        if not allcookies.get('_id') or allcookies['_id'] == '':
            return "", True
        else:
            return "", False


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
