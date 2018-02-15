import dash_html_components as html

HEADER_NOT_LOGIN = html.Div([
    html.Div([
        html.Div([
            html.A('Tasker', href='/', className='navbar-brand')
        ], className='navbar-header'),

        html.Div([
            html.Ul([
                html.Li(
                    html.A('Sign up', href='/signup')
                )
            ], className='nav navbar-nav navbar-right')
        ], className='collapse navbar-collapse')
    ], className='container-fluid')],
className='navbar navbar-default')

HEADER_LOGIN = html.Div([
    html.Div([
        html.Div([
            html.A('Tasker', href='/', className='navbar-brand')
        ], className='navbar-header'),

        html.Div([
            html.Ul([
                html.Li(
                    html.A('Profile', href='/profile'),
                ),
                html.Li(
                    html.A('Log out', href='/logout'),
                )
            ], className='nav navbar-nav navbar-right')
        ], className='collapse navbar-collapse')
    ], className='container-fluid')],
className='navbar navbar-default')
