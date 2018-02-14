from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

content = r"""
<style>
.wrapper {
display: flex;
}
.column {
display: flex;
flex-direction: column;
}
.column > div {
font-size: 4vh;
color: white;
background: royalblue;
margin: .1em;
padding: .3em 1em;
border-radius: 3px;
flex: 1;
}
</style>
<div class="wrapper">
<div class="column">
<div>1</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
<div>5</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
<div>5</div>
<div>6</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
<div>5</div>
<div>6</div>
<div>7</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
<div>5</div>
<div>6</div>
<div>7</div>
<div>8</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
<div>5</div>
<div>6</div>
<div>7</div>
<div>8</div>
<div>9</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
<div>5</div>
<div>6</div>
<div>7</div>
<div>8</div>
<div>9</div>
<div>10</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
<div>5</div>
<div>6</div>
<div>7</div>
<div>8</div>
<div>9</div>
<div>10</div>
<div>11</div>
</div>
<div class="column">
<div>1</div>
<div>2</div>
<div>3</div>
<div>4</div>
<div>5</div>
<div>6</div>
<div>7</div>
<div>8</div>
<div>9</div>
<div>10</div>
<div>11</div>
<div>12</div>
</div>
</div>
"""

layout = html.Div([
    html.H3('App 1'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Br(),

    html.Div(id='raw'),
    html.Br(),

    dcc.Link('Go to App 2', href='/apps/app2')
    #html.Br(),
    #html.A('Go to App 2', href="/apps/app2")
])

@app.callback(
    Output('raw', 'children'),
    [Input('app-1-dropdown', 'value')])
def show_display(value):
    value = str(value)

    #return 'You have selected "{}"'.format(value)
    #return raw_html(content)
    return html.Iframe(
        sandbox='',
        seamless=True,
        width= '100%',
        height='1000',
        srcDoc=content,
        style = {
            'border-style': 'none'
        }
    )
