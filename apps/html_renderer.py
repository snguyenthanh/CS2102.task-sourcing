import dash_html_components as html

def iframe(content, page_height=1000):
    return html.Iframe(
        sandbox='allow-top-navigation allow-scripts allow-popups-to-escape-sandbox allow-popups allow-same-origin allow-forms allow-modals allow-pointer-lock allow-modals allow-orientation-lock',
        seamless=True,
        width= '100%',
        height=page_height,
        srcDoc=content,
        style = {
            'border-style': 'none'
        })
