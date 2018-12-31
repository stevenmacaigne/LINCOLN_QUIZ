import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app, df
from apps import stat, home, mail, yammer
import pandas as pd
import datetime

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.P("USER_ID"),
    dcc.Input(id="id", value="enter user id here"),
    # add button
    html.Div(
        html.Span("CHECK USER",
              id="check_user",
              n_clicks=0,
              className="button button--primary",
              style={
                    "height": "36",
                    "width": "120",
                    "background": "#119DFF",
                    "border": "1px solid #DCDCDC",
                    "color": "white",
              },
        ),
        style={"margin-top":"47px"}
    ),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname'),
              ],
              [
                State('id', 'value')
              ]
)
def display_page(pathname, user_id):
    if pathname == '/':
        
        print(df)
        return stat.layout
    elif pathname == '/home':
        dat = datetime.datetime.now()
        df.loc[len(df)] = [str(user_id), dat, "home"]
        return home.layout
    elif pathname == '/mail':
        dat = datetime.datetime.now()
        df.loc[len(df)] = [str(user_id), dat, "mail"]
        return mail.layout
    elif pathname == '/yammer':
        dat = datetime.datetime.now()
        df.loc[len(df)] = [str(user_id), dat, "yammer"]
        return yammer.layout
    else:
        return '404'
    
@app.callback(Output('id', 'disabled'),
              [Input('check_user', 'n_clicks'),
              ],
              [
                State('id', 'value')
              ]
)
def check_user(n_clicks, user_id):
    print("checking user")
    if(user_id in df["id"]):
        return(True)
    else:
        return(False)

if __name__ == '__main__':
	app.run_server(debug=True, port=4141)


