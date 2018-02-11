import dash
from secret.hash import generate_new_token

app = dash.Dash()
server = app.server

app.title='Task Sourcing'
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
