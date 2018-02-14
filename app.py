import dash
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = dash.Dash()
server = app.server

app.title='Task Sourcing'
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
