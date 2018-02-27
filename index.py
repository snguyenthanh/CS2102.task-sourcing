from dash.dependencies import Input, Output, Event, State
import dash_core_components as dcc
import dash_html_components as html
import os
import flask

from app import app
from apps import app1, app2, sample_app
from apps.login import signup
from apps.html_renderer import get_header, get_footer

from get_data.from_sql.queries.select import get_person_with_pwd
from get_data.from_sql.queries.create import create_all_tables
from get_data.from_sql.queries.insert import insert_all_statuses, insert_all_categories
from get_data.from_sql.postgres_client import close_db

# The top layout of every page
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.Div(id='user-info',style={'display': 'none'}),

    html.Div(id='page-header'),

    html.Div(id='page-content'),

    get_footer(),

    # Default CSS
    html.Link(
        rel='stylesheet',
            href='/static/bWLwgP.css'
            ),
    # Loading CSS
    html.Link(
        rel='stylesheet',
            href='/static/brPBPO.css'
            ),
    # Bootstrap
    html.Link(
        rel='stylesheet',
            href='/static/bootstrap.min.css'
            ),
])

login_layout =  html.Div([
        html.Div([
            html.Label("Username:",style={'font-weight': 'bold', 'marginRight': 185}),
            dcc.Input(id='login-username', value='', type='text',
                style={'width': '20%',
                    'display': 'inline-block',
                    'marginLeft': 20})
        ], style={'text-align': 'center'}),
        html.Br(),

        html.Div([
            html.Label("Password:",style={'font-weight': 'bold', 'marginRight': 185}),
            dcc.Input(id='login-password', value='', type='password',
                style={'width': '20%',
                    'marginLeft': 20})
        ], style={'text-align': 'center'}),
        html.Br(),

        html.Div([
            html.Button(id='login-button', children='Login')
        ], style={'text-align': 'center'}),
        html.Br(),

        html.Div([
            html.A('or create an account', href="/signup")
        ], style={'text-align': 'center'})
])

@app.callback(
    Output('user-info', 'children'),
    events=[Event('login-button', 'click')],
    state=[State('login-username', 'value'),
        State('login-password', 'value')]
)
def login_user(username, password):
    user = ""
    try:
        user = get_person_with_pwd(username, password)[0]
    except:
        pass
    return user

@app.callback(
    Output('page-header', 'children'),
    [Input('user-info', 'children')]
)
def show_header(user):
    user = str(user)

    if user == "None" or user == "":
        return get_header()
    else:
        return get_header(True)

## Static CSS folder
@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return flask.send_from_directory(static_folder, path)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname'),
              Input('user-info', 'children')])
def display_page(pathname, user):
    user = str(user)
    if pathname == '/signup':
        return signup.layout

    # Temporarily disable user validation
    #if user == "None" or user == "" or pathname == '/login' or pathname == '/logout':
    #    return login_layout

    # If user is valid
    if pathname == '/apps/app1' or pathname == r'/':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/sample':
        return sample_app.layout
    else:
        return '404'

def init_database():
    # Create
    create_all_tables()

    # Insert
    insert_all_statuses()
    insert_all_categories()

if __name__ == '__main__':
    init_database()

    try:
        app.run_server(debug=True, port=5000)
    finally: # If the server goes down, shut down the connections with the database
        close_db()
