import os
import pandas as pd
import dash
import flask
from dash.dependencies import Input, Output
import dash_bio as dashbio
from dash import html
from dash import dcc


PUBLIC_URL_PREFIX = os.getenv("PUBLIC_URL_PREFIX", "")


#: The Flask application to use.
app_flask = flask.Flask(__name__)

# Setup URL prefix for Flask.
app_flask.config["APPLICATION_ROOT"] = "%s/" % PUBLIC_URL_PREFIX

#: The Dash application to run.
app = dash.Dash(
    __name__,
    # Use our specific Flask app
    server=app_flask,
    # The visualization will be served below "/dash"
    requests_pathname_prefix="%s/" % PUBLIC_URL_PREFIX,
)

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
    'manhattan_data.csv'
)

app.layout = html.Div([
    'Threshold value',
    dcc.Slider(
        id='default-manhattanplot-input',
        min=1,
        max=10,
        marks={
            i: {'label': str(i)} for i in range(10)
        },
        value=6
    ),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='default-dashbio-manhattanplot',
            figure=dashbio.ManhattanPlot(
                dataframe=df
            )
        )
    )
])

@app.callback(
    Output('default-dashbio-manhattanplot', 'figure'),
    Input('default-manhattanplot-input', 'value')
)
def update_manhattanplot(threshold):

    return dashbio.ManhattanPlot(
        dataframe=df,
        genomewideline_value=threshold
    )

if __name__ == '__main__':
    app.run_server()