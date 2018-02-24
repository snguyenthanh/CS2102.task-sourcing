import dash_html_components as html

from views.partials.header import HEADER_NOT_LOGIN, HEADER_LOGIN
from views.partials.footer import FOOTER

def get_header(hasLoggedIn=False):
    if hasLoggedIn:
        return HEADER_LOGIN
    else:
        return HEADER_NOT_LOGIN

def get_footer():
    return iframe(FOOTER, 50)

def iframe(content, page_height=1000):
    return html.Iframe(
        sandbox='allow-top-navigation allow-scripts allow-popups-to-escape-sandbox allow-popups allow-same-origin allow-forms allow-modals allow-pointer-lock allow-modals allow-orientation-lock allow-top-navigation-by-user-activation',
        seamless=True,
        width= '100%',
        height=page_height,
        srcDoc=content,
        style = {
            'border-style': 'none'
        })
