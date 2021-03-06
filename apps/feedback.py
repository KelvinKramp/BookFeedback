# IMPORT MODULES
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

score = [{'label': 'Strongly agree', 'value': '1'}, {'label': 'Agree', 'value': '2'}, {'label': 'Neutral', 'value': '3'}, {'label': 'Disagree', 'value': '4'}, {'label': 'Strongly disagree', 'value': '5'}]
style_score = {'display': 'inline-block', 'text-align': 'center', 'display': 'flex',
                                           'justify-content': 'space-evenly', 'width': '30%'}
labelStyle_score = {'display': 'inline-block', 'text-align': 'right','width': '100%',}

register_introduction_text = ""
explanation = "To complete the feedback form please fill in your name and e-mail or log in with Google. This allows me to know who you are and get back in contact with you if I have any additional questions."
introduction_text = ""
open_question_1 = "Which chapter was the most interesting chapter and why?"
open_question_2 = "Did you get stuck/disinterested while reading? and if yes where and why?"
open_question_3 = "What could be improved in the illustrations?"
open_question_4 = "If you think it was incomplete can you tell me what you think was missing?"
open_question_5 = "Is there something you missed in the interviews?"
open_question_6 = "Is there someone you think should have been interviewed?"
open_question_7 = "Do you have any comments?"

Q1 = "The text had flow"
Q2 = "The text was enjoyable to read"
Q3 = "The text was understandable"
Q4 = "The ideas were interesting"
Q5 = "The text was too long"
Q6 = "Were the illustrations helpfulll?"
Q7 = "Do you think there were things missing?"
Q8 = "The interviews helped understand the different perspectives on partner dance?"

layout = html.Div(children=[
        html.Br(),
        dbc.Row([
            dbc.Col(html.H5(introduction_text, style={'width': 'fit-content', 'overflow-wrap': 'break-word'}),
                    width={"size": 10, "offset": 1},
                    )], ),
        html.Br(),

        ## Readability comprehensibility
        dbc.Row([
            html.H4("Readability/comprehensibilty",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
        ]),
        dbc.Row([
            html.Br(),
        ]),
        dbc.Row(children=[
            html.H5(Q1,
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
            html.H5(Q2,
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
            html.H5(Q3,
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
            html.H5(Q4,
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
            html.H5(Q5,
                    style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
            dcc.RadioItems(
                options=score,
                id='5',
                value='',
                labelStyle=labelStyle_score,
                style=style_score,
            ),
        ], ),
        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_1,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea1',
                    maxLength='1999',
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
                    maxLength='1999',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),
        html.Br(),

        ## Illustrations
        dbc.Row([
            html.H4("Illustrations",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
        ]),
        dbc.Row([
            html.Br(),
        ]),
        dbc.Row(children=[
            html.H5(Q6,
                    style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
            dcc.RadioItems(
                options=score,
                id='6',
                value='',
                labelStyle=labelStyle_score,
                style=style_score,
            ),
        ], ),
        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_3,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea3',
                    maxLength='1999',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),
        html.Br(),

        # c5
        # o3
        ## Completeness
        dbc.Row([
            html.H4("Completeness",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
        ]),
        dbc.Row([
            html.Br(),
        ]),
        dbc.Row(children=[
            html.H5(Q7,
                    style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
            dcc.RadioItems(
                options=score,
                id='7',
                value='',
                labelStyle=labelStyle_score,
                style=style_score,
            ),
        ], ),
        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_4,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea4',
                    maxLength='1999',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),
        html.Br(),

        # o4
        # c6
        # Interviews
        dbc.Row([
        html.H4("Interviews",
                    style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
        ]),
        html.Br(),
        dbc.Row(children=[
            html.H5(Q8,
                    style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
            ]),
            dbc.Row([
                dcc.RadioItems(
                    options=score,
                    id='8',
                    value='',
                    # labelStyle=labelStyle_score,
                    labelStyle = {"display": "inline-block", 'justify-content': 'space-evenly', 'text-align': 'center', 'width': '100%',},
                    style={"display": "inline-block", 'text-align': 'center',
                                 'justify-content': 'space-evenly', 'width': '100%'},
                ),
            ]),
        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_5,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea5',
                    maxLength='1999',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_6,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea6',
                    maxLength='1999',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            html.H5(
                "(If you have been interviewed and you encountered any errors in your own interview don't hesitate to notify me personally.)",
                style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
        ], ),
        html.Br(),

        # Open comments
        html.H4("Open comments",
                style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
        dbc.Row([
            html.Br(),
        ]),
        dbc.Row(children=[
            dbc.Col(
                html.H5(open_question_7,
                        style={"display": "inline-block", "width": "100%", },
                        ), width={"size": 10, "offset": 2}, ), ]),
        dbc.Row(children=[
            dbc.Col(
                dbc.ModalBody(children=(dcc.Textarea(
                    id='textarea7',
                    maxLength='1999',
                    value='',
                    spellCheck=True,
                    style={"display": "flex", 'justifyContent': 'center', 'width': '80%', 'height': 100},
                ),),
                ), width={"size": 10, "offset": 2}, ), ]),




        # BUTTONS AND MODALS
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
                dbc.ModalHeader("Feedback form submitted."),
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
                dbc.ModalHeader("Feedback form", close_button=False, style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                dbc.ModalFooter(children=[
                    html.Div(register_introduction_text, style={'text-align': 'justify','width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    html.Div(""""""),
                    html.Div(explanation, style={'text-align': 'justify','width': '100%', 'display': 'flex', 'justify-content':'center'}),
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
                    #html.Div("Or login with google to automatically register", style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    dbc.Row(children=[
                        dbc.Button("Register with Google", id='google-login', className="ml-auto", n_clicks=0,
                                   style={'width': '100%', 'align':'center', 'display': 'flex', 'justify-content': 'center'}),
                    ],style={'width': '100%', 'display': 'flex', 'justify-content':'center'}),
                    ])
                ],
            is_open=False,
            id="modal3",
            style={"white-space": "break-spaces"},
            backdrop=False
        ),
    ])
