from dash.dependencies import Input, Output,State,Event
import dash_html_components as html
import dash_core_components as dcc

from get_data.from_sql.queries.insert import insert_new_person
from get_data.from_sql.queries.select import get_person, get_email

from validate_email import validate_email
from app import app

layout = html.Div([
    html.H2('Sign up'),

    html.Div(id='signup-error-msg'),

    html.Div(id='signup-content'),

    html.Br()
])

def isValidString(text):
    if (not text) or text == "":
        return False

    try:
        for char in text:
            if char not in ['_', '.'] and not char.isalnum():
                return False
    except:
        return False

    return True

def isNotExistPerson(username):
    try:
        if username == get_person(username)[0]:
            return False
    except:
        pass
    return True

def isValidPassword(pwd):
    try:
        if len(pwd) < 8:
            return False
        if not isValidString(pwd):
            return False
    except:
        return False
    return True

def isValidEmail(email):
    try:
        parsedEmail = validate_email(email)
    except:
        return False
    return parsedEmail

def isNotExistEmail(email):
    try:
        email_queried = get_email(email)
    except:
        return False
    try:
        if email == email_queried[0]:
            return False
    except:
        pass

    return True

def checkValidAccount(username, pwd, pwd_again, email):
    if not isValidString(username):
        return html.Div("Username cannot contain non-alphanumeric characters.")
    if not isNotExistPerson(username):
        return html.Div("Username {} has already been taken.".format(username))
    if not isValidPassword(pwd):
        return html.Div("Password is invalid. It must have at least 8 characters and only contain alphanumeric characters.")
    if not isValidPassword(pwd_again):
        return html.Div("Retyped password is invalid. It must have at least 8 characters and only contain alphanumeric characters.")
    if pwd != pwd_again:
        return html.Div("Password and retyped password mismatch.")
    if not isValidEmail(email):
        return html.Div("Email is invalid.")
    if not isNotExistEmail(email):
        return html.Div("An account has already been created with `{}`. Please use another email.".format(email))

    # If all the fields are valid, insert the person and return "Success" page
    insert_new_person(username, pwd, email)

    return html.Div([
                html.H3("Your account has been created successfully."),
                html.Div("Username: {}".format(username)),
                html.Br()
            ])

@app.callback(
    Output('signup-content', 'children'),
    [Input('signup-error-msg', 'children')]
)
def signup_form(msg):
    layout = html.Div([

        html.Div([
            html.Label("Choose your username:",style={'font-weight': 'bold', 'marginRight': 90}),
            dcc.Input(id='signup-username', value='', type='text',
                style={'width': '20%',
                    'display': 'inline-block',
                    'marginLeft': 20})
        ], style={'text-align': 'center'}),
        html.Br(),

        html.Div([
            html.Label("Create a password:",style={'font-weight': 'bold', 'marginRight': 120}),
            dcc.Input(id='signup-password', value='', type='password',
                style={'width': '20%',
                    'marginLeft': 20})
        ], style={'text-align': 'center'}),
        html.Br(),

        html.Div([
            html.Label("Confirm your password:",style={'font-weight': 'bold', 'marginRight': 90}),
            dcc.Input(id='signup-password-again', value='', type='password',
                style={'width': '20%',
                    'marginLeft': 20})
        ], style={'text-align': 'center'}),
        html.Br(),

        html.Div([
            html.Label("Email:",style={'font-weight': 'bold', 'marginRight': 215}),
            dcc.Input(id='signup-email', value='', type='text',
                style={'width': '20%',
                    'marginLeft': 20})
        ], style={'text-align': 'center'}),
        html.Br(),

        html.Div([
            html.Button(id='signup-button', children='Create an account')
        ], style={'text-align': 'center'}),
    ])

    if "Your account has been created successfully." in str(msg):
        layout = html.Div([
            html.A('Click here to redirect to main', href="/apps/app1")
        ])

    return layout

@app.callback(
    Output('signup-error-msg', 'children'),
    events=[Event('signup-button', 'click')],
    state=[State('signup-username', 'value'),
            State('signup-password', 'value'),
            State('signup-password-again', 'value'),
            State('signup-email', 'value')]
)
def signup_check(username, password, password_again, email):
    # Check for empty fields
    try:
        if not username or username == "":
            return html.Div("Username cannot be empty")
        if not password or password == "":
            return html.Div("Password cannot be empty")
        if not password_again or password_again == "":
            return html.Div("Retyped password cannot be empty")
        if not email or email == "":
            return html.Div("Email cannot be empty")
    except:
        return html.Div("There exists an unsupported character in the signup form.")

    return checkValidAccount(str(username), str(password), str(password_again), str(email))
