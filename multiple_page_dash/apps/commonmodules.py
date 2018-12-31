import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def get_header(text):
    header = html.Div(
        [
            html.Div(
                [
                    html.H1(text)
                ]
            ),       
        ], 
    )
    return header

def get_menu_from_stat():
    menu = html.Div(
        [
            html.Div(dcc.Link('Stat', href='/')),
            html.Div(dcc.Link('Home', href='/home')),
        ], 
    )
    return menu 


def get_menu():
    menu = html.Div(
        [
            html.Div(dcc.Link('Home', href='/home')),
            html.Div(dcc.Link('Mail', href='/mail')),
            html.Div(dcc.Link('Yammer', href='/yammer')),
            html.Div(dcc.Link('Back to stat with my path', href='/')),
        ], 
    )
    return menu 