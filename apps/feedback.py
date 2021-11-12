# IMPORT MODULES
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from app import app
from apps import priv_pol, term_cond, feedback, auth, login
import json
from http import cookies
import dash

C = cookies.SimpleCookie()

score = [{'label': 'Strongly agree', 'value': '1'}, {'label': 'Agree', 'value': '2'}, {'label': 'Neutral', 'value': '3'}, {'label': 'Disagree', 'value': '4'}, {'label': 'Strongly disagree', 'value': '5'}]
style_score = {'display': 'inline-block', 'text-align': 'center', 'display': 'flex',
                                           'justify-content': 'space-evenly', 'width': '30%'}
labelStyle_score = {'display': 'inline-block', 'text-align': 'right','width': '100%',}

introduction_text = """You've received a copy because you have contributed directly or indirectly to the writing or because you were just genuinely interested in what I've written down. 
                                        I didn't explicitely tell you that it wasn't the final version because I wanted you to read as if it was the real thing. 
                                        If you've had the time to read it, or parts of it, I would love to hear your opinion and use it in the final version before I
                                        go public."""
open_question_1 = "What did you think was the most interesting chapter and why?"
open_question_2 = "Did you get stuck/disinterested while reading? and if yes where and why?"
open_question_3 = "If you think it was incomplete can you tell me what you think was missing?"
open_question_4 = "Do you have any other comments?"
global state_file
state=True # state of the login modal window at opening the website
state_file = 'state_modal.json'
with open(state_file, 'w') as f:
    f.write('{"state": "True"}')

layout = html.Div(children=[
        html.Br(),
        dbc.Row([
            dbc.Col(html.H5(introduction_text, style={'width': 'fit-content', 'overflow-wrap': 'break-word'}),
                    width={"size": 10, "offset": 1},
                    )], ),
        html.Br(),
        dbc.Row([
            html.H4("Multiple choice questions",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
        ]),
        dbc.Row(children=[
            html.H5("The text was understandable",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
            dcc.RadioItems(
                options=score,
                id='1',
                value='',
                labelStyle=labelStyle_score,
                style=style_score,
            ),
        ], ),
        dbc.Row(children=[
            html.H5("The text had flow",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
            dcc.RadioItems(
                options=score,
                id='2',
                value='',
                labelStyle=labelStyle_score,
                style=style_score,
            ),
        ], ),
        dbc.Row(children=[
            html.H5("The ideas were interesting",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
            dcc.RadioItems(
                options=score,
                id='3',
                value='',
                labelStyle=labelStyle_score,
                style=style_score,
            ),
        ], ),
        dbc.Row(children=[
            html.H5("The text was too long",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
            dcc.RadioItems(
                options=score,
                id='4',
                value='',
                labelStyle=labelStyle_score,
                style=style_score,
            ),
        ], ),
        dbc.Row(children=[
            html.H5("The book was complete",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
            dcc.RadioItems(
                options=score,
                id='5',
                value='',
                labelStyle=labelStyle_score,
                style=style_score,
            ),
        ], ),
        html.Br(),
        dbc.Row([
            html.H4("Open questions",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
        ]),
        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_1,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea1',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),

        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_2,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea2',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),

        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_3,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea3',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),

        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_4,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea4',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),
        html.Br(),
        html.Div([
            dbc.Button("Submit", id="submit-button", className="ml-auto", n_clicks=0, style={'width': '150%'},
                       ),
        ], style={'margin-bottom': '10px',
                  'textAlign': 'center',
                  'width': '220px',
                  'margin': 'auto'}
        ),
        html.Br(),
        html.Div('', id='empty-div-output'),
        dbc.Modal(
            [
                dbc.ModalHeader("Do you want to submit the feedback?"),
                dbc.ModalFooter(children=[
                    dbc.Button("Submit", id="save", className="ml-auto", n_clicks=0),
                ]
                ),
            ],
            is_open=False,
            id="modal",
            style={"white-space": "break-spaces"},
            backdrop=False
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("You have submitted. Thank you for giving your feedback"),
                dbc.ModalFooter(children=[
                    dbc.Button("Close", id='close', className="ml-auto", n_clicks=0),
                ]
                ),
            ],
            is_open=False,
            id="modal2",
            style={"white-space": "break-spaces"},
            backdrop=False
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("Register", style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                dbc.ModalFooter(children=[
                    html.Div("Fill in your information to register", style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    dbc.Row(children=[
                        html.Div("First name"),
                    ],style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    dbc.Row(children=[
                    dcc.Input(
                                id="name",
                                type="text",
                    ),],style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    dbc.Row(children=[
                        html.Div("E-mail"),
                    ],style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    dbc.Row(children=[
                    dcc.Input(
                        id="email",
                        type="email",
                    ),],style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    dbc.Row(children=[
                        dbc.Button("Register", id='register-manual', className="ml-auto", n_clicks=0,
                                   style={'width': '100%', 'align': 'center', 'display': 'flex',
                                          'justify-content': 'center'}),
                    ],style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    html.Div("Or login with google to automatically register", style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    dbc.Row(children=[
                        dbc.Button("Google", id='google-login', className="ml-auto", n_clicks=0,
                                   style={'width': '100%', 'align':'center', 'display': 'flex', 'justify-content': 'center'}),
                    ],style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    ])
                ],
            is_open=state,
            id="modal3",
            style={"white-space": "break-spaces"},
            backdrop=False
        ),
    ])

### CALLBACKS ## the numbers are LETTER O followed by a number
@app.callback(
    Output("modal", "is_open"),
    Output("modal2", "is_open"),
    [Input("1", "value"),
     Input('2', 'value'),
     Input('3', 'value'),
     Input('4', 'value'),
     Input('5', 'value'),
     Input('textarea1', 'value'),
     Input('textarea2', 'value'),
     Input('textarea3', 'value'),
     Input('textarea4', 'value'),
     Input('submit-button', 'n_clicks'),
     Input('save', 'n_clicks'),
     Input('close', 'n_clicks')],
    [State("modal", "is_open"),
     State("modal2", "is_open")],
)
def submit(Question1, Question2, Question3, Question4, Question5, text1, text2, text3, text4, submitclick, save, close, is_open, is_open2):
    if save == 0 and submitclick== 1:
        return not is_open, is_open2
    elif submitclick >1:
        return is_open, not is_open2
    elif close:
        return not is_open, not is_open2
    elif save == 1 and submitclick==1:
        print(Question1, Question2, Question3, Question4, Question5, text1, text2, text3, text4)
        return is_open, not is_open2
    return is_open, is_open2

@app.callback(
    Output("hidden_div_for_redirect_callback", "children"),
    Output("modal3", "is_open"),
    [Input('google-login', 'n_clicks'),
     Input('register-manual', 'n_clicks'),
     Input('name', 'value'),
     Input('email', 'value')],
    [State("modal3", "is_open")],
)
def google_fb_login(a,b, name, email, c,):
    print(a,b, name, email, c,)
    import flask
    allcookies = dict(flask.request.cookies)
    if a==1 and b==0:
        auth = login.AuthPage()
        auth_url = auth.GET("google")

        return dcc.Location(href=auth_url,
                           id="someid"), False
    elif b==1:
        dash.callback_context.response.set_cookie('_id', "register_manual")
        dash.callback_context.response.set_cookie('_profile', "'{"+"name"+":"+ str(name)+"}'")
        return "", False
    else:
        if not allcookies.get('_id') or allcookies['_id'] == '':
            return "", True
        else:
            return "", False
