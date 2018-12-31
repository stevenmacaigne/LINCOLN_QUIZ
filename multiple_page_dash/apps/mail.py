import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps import commonmodules

from app import app


layout = html.Div([
    commonmodules.get_header("Mail Page"),
    commonmodules.get_menu(),
])