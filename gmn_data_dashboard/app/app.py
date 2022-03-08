""""""
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output

# Imports
from datetime import datetime
from gmn_python_api.data_directory import get_daily_file_content_by_date
from gmn_python_api.trajectory_summary_reader import \
    read_trajectory_summary_as_dataframe, DATETIME_FORMAT

import plotly.io as pio
import plotly.express as px

pio.templates.default = "plotly_dark"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Load the contents of a specific daily trajectory summary file into a Pandas DataFrame
trajectory_summary_file_content = get_daily_file_content_by_date(datetime(2021, 6, 24))
trajectory_summary_dataframe = read_trajectory_summary_as_dataframe(
    trajectory_summary_file_content)

print(trajectory_summary_dataframe.info())

# Layout
app.layout = html.Div([
    dcc.Dropdown(options={
        '2021-06-24': datetime(2021, 6, 24),
        '2021-06-25': datetime(2021, 6, 25),
        '2021-06-26': datetime(2021, 6, 26)
    }, value='2021-06-24', id='demo-dropdown'),
    dcc.Graph(id="map",
              figure=px.scatter_geo(trajectory_summary_dataframe,
                                    lat="BEThel (deg)",
                                    lon="LAMhel (deg)")),
    html.Div(id='dd-output-container')
])


@app.callback(
    Output('map', 'figure'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    global trajectory_summary_dataframe
    trajectory_summary_file_content = get_daily_file_content_by_date(
        datetime.strptime(value, "%Y-%m-%d"))
    trajectory_summary_dataframe = read_trajectory_summary_as_dataframe(
        trajectory_summary_file_content)
    return px.scatter_geo(trajectory_summary_dataframe,
                          lat="BEThel (deg)",
                          lon="LAMhel (deg)")


if __name__ == "__main__":
    import os

    debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True
    app.run_server(host="0.0.0.0", port=8050, debug=debug)
