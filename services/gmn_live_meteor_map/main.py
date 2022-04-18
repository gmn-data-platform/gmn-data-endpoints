""""""
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
import dash_leaflet as dl

# Imports
from datetime import datetime
from gmn_python_api.data_directory import get_daily_file_content_by_date
from gmn_python_api.trajectory_summary_reader import \
    read_trajectory_summary_as_dataframe

app = dash.Dash(__name__)

# Load the contents of a specific daily trajectory summary file into a Pandas DataFrame
trajectory_summary_file_content = get_daily_file_content_by_date(datetime(2021, 6, 24))
trajectory_summary_dataframe = read_trajectory_summary_as_dataframe(
    trajectory_summary_file_content)

print(trajectory_summary_dataframe.info())

# Layout
app.layout = html.Div([
    dl.Map(dl.TileLayer(), style={'width': '1000px', 'height': '500px'}),
    html.Div([
        html.Div([
            html.H3('Meteors'),
            html.Ul([
                html.Li(
                    trajectory_summary_dataframe.iloc[0]['Beginning (Julian date)']),
                html.Li(
                    trajectory_summary_dataframe.iloc[1]['Beginning (Julian date)']),
                html.Li(trajectory_summary_dataframe.iloc[2]['Beginning (Julian date)'])
            ])
        ], className='col-md-4'),
    ], className='row'),
])

if __name__ == "__main__":
    import os

    debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True
    app.run_server(host="0.0.0.0", port=8050, debug=debug)
