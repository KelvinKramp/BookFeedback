# IMPORT MODULES
from dash import html
from dash.dependencies import Input, Output, State
from dash import dcc
import dash_bootstrap_components as dbc
from apps import priv_pol, term_cond, thanks, login # feedback app is imported in the callback because otherwise error due to to late loading of form
from app import app
import urllib
import json
from flask import request
import dash
from app import db, Feedback_Book, Report_Bug, Buy_Hardcover
from app import server # = necessary import
import datetime
from datetime import datetime as dt
from datetime import timezone
import time
import os

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Paypal", href="https://paypal.me/urbankizbook?country.x=NL&locale.x=nl_NL", target="_blank"),
                dbc.DropdownMenuItem("Buy photo illustrated hardcover copy", id="buy", n_clicks=0, href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Support my writing",
        ),
        dbc.NavItem(dbc.NavLink("Report a bug", id='report-bug', n_clicks=0)),
        # dbc.NavItem(dbc.NavLink("Logout", id="logout", href="/logout")),
    ],
    brand="Feedback form - Urban kiz: a new vision on partner dance",
    brand_href="/",
    color="primary",
    dark=True,
    sticky=True,
)

app.title = 'Feedback'
app.layout = html.Div(children=[
                            navbar,
                            dcc.Location(id='url', refresh=False),
                            html.Div(id="page-content", children=[
                            ]),
                            dbc.Row([
                                    dcc.Link('Terms and conditions', href='/apps/term_cond', style={"color":"white"}),
                                    dbc.Col('', width='1'),
                                    dcc.Link('Privacy policy', href='/apps/priv_pol', style={"color":"white"}),
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
    from apps import feedback
    # placed import feedback over here because otherwise the loading of the callback is going to be faster then
    # the layout loading, causing an error of input not found of callback
    allcookies = dict(request.cookies)
    # print("printing allcookies for displaying page")
    # print(allcookies)
    if "/report-bug" in href:
        return feedback.layout
    elif '/apps/priv_pol' in href:
        return priv_pol.layout
    elif '/apps/term_cond' in href:
        return term_cond.layout
    elif ("/thanks" in href) or allcookies.get('_close'):
        dash.callback_context.response.set_cookie('_close', "submitted_form")
        return thanks.layout
    elif allcookies.get('_id'):
        return feedback.layout
    elif '/auth/google/callback' in href:
        # print("google authenticated")
        url_dict = urllib.parse.parse_qs(href)
        code_item = next(iter(url_dict))
        code = url_dict[code_item][0]
        callback = login.AuthCallbackPage()
        callback.GET('google', code)
        return feedback.layout
    elif "/logout" in href:
        callback = login.LogoutPage()
        callback.GET()
        time.sleep(2)
        allcookies = dict(request.cookies)
        # print("this are the cookies after logging out")
        # print(allcookies)
        return feedback.layout
    else:
        return feedback.layout


@app.callback(
    Output("modal-bug", "is_open"),
    [Input("report-bug", "n_clicks"), Input("send-email", "n_clicks")],
    [State("modal-bug", "is_open"), State("textarea", "value")],
)
def report_bug_modal(n1, n2, is_open, text):
    if n1 > n2:
        return not is_open
    elif (n2 == n1) and len(text)>0:
        print("TEST1: REPORTING BUG")
        allcookies = dict(request.cookies)
        # print(allcookies)
        try:
            d = allcookies['_profile']
            d = json.loads(d)
            name = d['name']
            email = d['email']
            # print(name, email, text)
            report_bug = Report_Bug(name=name, email=email, bug=text, time=(str(dt.now(datetime.timezone.utc).day)+"-"+str(dt.now(datetime.timezone.utc).month)+"-"+str(dt.now(datetime.timezone.utc).year)))
        except Exception as e:
            print(e)
            name = "Unknown"
            email = "Unknown"
            # print(name, email, text)
            report_bug = Report_Bug(name=name, email=email, bug=text, time=(str(dt.now(datetime.timezone.utc).day)+"-"+str(dt.now(datetime.timezone.utc).month)+"-"+str(dt.now(datetime.timezone.utc).year)))
        db.session.add(report_bug)
        db.session.commit()
        return not is_open
    elif n1 >0 and (n1 == n2):
        return not is_open
    else:
        return is_open

@app.callback(
    Output("modal-hardcover", "is_open"),
    [Input("buy", "n_clicks"), Input("close-hardcover", "n_clicks")],
    [State("modal-hardcover", "is_open")],
)
def hardcover_modal(n1, n2, is_open):
    if n1 ==1 and n2 ==0:
        allcookies = dict(request.cookies)
        time = (str(dt.now(datetime.timezone.utc).day)+"-"+str(dt.now(datetime.timezone.utc).month)+"-"+str(dt.now(datetime.timezone.utc).year))
        print("TEST2: HARDCOVER")
        try:
            d = allcookies['_profile']
            d = json.loads(d)
            name = d['name']
            email = d['email']
            # print(name, email, True)
            buy_hardcover = Buy_Hardcover(name=name, email=email, buy=True, time=time)
        except Exception as e:
            print(e)
            name = "Unknown"
            email = "Unknown"
            # print(name, email, True)
            buy_hardcover = Buy_Hardcover(name=name, email=email, bug=True, time=time)
        db.session.add(buy_hardcover)
        db.session.commit()
        return not is_open
    if n1==1 and n2==1:
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
     Input('8', 'value'),
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
def submit(Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, text1, text2, text3, text4, text5, text6, text7, submitclick, save, close, is_open, is_open2):
    if save == 0 and submitclick== 1:
        return not is_open, is_open2, None
    elif submitclick >1:
        return is_open, not is_open2, None
    elif close:
        return not is_open, not is_open2, dcc.Location(href="/thanks",
                           id="someid")
    elif save == 1 and submitclick==1:
        try:
            print("TEST3: HARDCOVER")
            allcookies = dict(request.cookies)
            d = allcookies['_profile']
            d = json.loads(d)
            name = d['name']
            email = d['email']
            list_questions = [Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8]
            list_new = [None if i == "" else int(i) for i in list_questions]
            Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8 = list_new
            feedback_info = Feedback_Book(name=name, email=email, Q_C1=Question1, Q_C2=Question2, Q_C3=Question3, Q_C4=Question4, Q_C5=Question5, Q_C6=Question6, Q_C7=Question7,  Q_C8=Question8, Q_open1=str(text1), Q_open2=str(text2), Q_open3=str(text3), Q_open4=str(text4), Q_open5=str(text5), Q_open6=str(text6), Q_open7=str(text7), time=(str(dt.now(datetime.timezone.utc).day)+"-"+str(dt.now(datetime.timezone.utc).month)+"-"+str(dt.now(datetime.timezone.utc).year)))
            db.session.add(feedback_info)
            db.session.commit()
        except Exception as e:
            print("Error occurred in commit to db try statement")
            error_file = "errors.json"
            with open(error_file, 'w') as f:
                f.write(str(e) + "\n")
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
    allcookies = dict(request.cookies)
    if a==1 and b==0:
        auth = login.AuthPage()
        auth_url = auth.GET("google")

        return dcc.Location(href=auth_url,
                           id="someid"), False
    elif a==0 and b>0 and (name != None or "")  and (email != None or ""):
        dash.callback_context.response.set_cookie('_id', "register_manual")
        dash.callback_context.response.set_cookie('_profile', '{'+'"name"'+':"'+ str(name)+'",'+'"email"'+':"'+ str(email)+'"}')
        time.sleep(2)
        return dcc.Location(href='/',
                           id="someid2"), False
    else:
        if not allcookies.get('_id') or allcookies['_id'] == '':
            return "", True
        else:
            return "", False


if __name__ == '__main__':
    if os.environ.get('ENV') == "DEVELOPMENT":
        app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
    else:
        app.run_server()