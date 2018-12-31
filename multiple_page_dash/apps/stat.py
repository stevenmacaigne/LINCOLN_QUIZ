import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from apps import commonmodules
import pandas as pd
import numpy as np

# plotly libraries
from plotly import graph_objs as go
from app import app, df


layout = html.Div([
    commonmodules.get_header("Stat Page"),
    commonmodules.get_menu_from_stat(),
    dcc.Graph(id="stat_layout"),
    html.Div("some value", style={"display":"none"} ,id="useless")
])


@app.callback(Output('stat_layout', 'figure'),
              [Input('useless', 'children'),
               Input("check_user", "n_clicks"),
              ],
              [State("id", "value"),
              ]
)
def display_stat(pathname, n_clicks, user_id):
    # make the barplot
    print("display stat")
    df["id"] = df["id"].astype(str)

    if(user_id in set(df["id"])):
        df_tmp = df.sort_values(["id", "time"], ascending=[True, True]).copy()
        df_tmp['time_leaded'] = df_tmp[df_tmp["id"].astype(str)!=user_id].groupby(['id'])['time'].shift(-1)#.dropna()
        df_tmp = df_tmp.dropna()
        df_tmp["time_spent_on_page"] = pd.to_datetime(df_tmp["time_leaded"]) -pd.to_datetime(df_tmp["time"])
        #df_tmp = df_tmp.groupby(["page"])\
        #.agg({"time_spent_on_page": lambda x: np.mean(x)})

        df_tmp2 = df.sort_values(["id", "time"], ascending=[True, True]).copy()
        df_tmp2['time_leaded'] = df_tmp2[df_tmp2["id"].astype(str)==user_id].groupby(['id'])['time'].shift(-1)#.dropna()
        df_tmp2 = df_tmp2.dropna()
        df_tmp2["time_spent_on_page"] = pd.to_datetime(df_tmp2["time_leaded"]) -pd.to_datetime(df_tmp2["time"])
        #df_tmp2 = df_tmp.groupby(["page"])\
        #.agg({"time_spent_on_page": lambda x: np.mean(x)})

        data_trace = []
        for pag in set(df_tmp["page"]):
            trace1 = go.Histogram(
                x=df_tmp["time_spent_on_page"].apply(lambda x: x.seconds / 60)[df_tmp["page"]==pag],
                opacity=0.75,
                name="All users: {}".format(pag)
            )
            data_trace.append(trace1)

        for pag in set(df_tmp["page"]):
            trace2 = go.Histogram(
                x=df_tmp2["time_spent_on_page"].apply(lambda x: x.seconds / 60)[df_tmp2["page"]==pag],
                opacity=0.75,
                name="Current user : {}".format(pag)
            )
            data_trace.append(trace2)
        
    else:
        df_tmp = df.sort_values(["id", "time"], ascending=[True, True]).copy()
        df_tmp['time_leaded'] = df_tmp.groupby(['id'])['time'].shift(-1)#.dropna()
        df_tmp = df_tmp.dropna()
        df_tmp["time_spent_on_page"] = pd.to_datetime(df_tmp["time_leaded"]) -pd.to_datetime(df_tmp["time"])
        #df_tmp = df_tmp.groupby(["page"])\
        #.agg({"time_spent_on_page": lambda x: np.mean(x)})

        data_trace = []
        for pag in set(df_tmp["page"]):
            trace1 = go.Histogram(
                x=df_tmp["time_spent_on_page"].apply(lambda x: x.seconds / 60)[df_tmp["page"]==pag],
                opacity=0.75,
                name="All users: {}".format(pag)
            )
            data_trace.append(trace1)
    
    #build a layout
    layout = go.Layout(
        margin=dict(l=40, r=30, b=70, t=0, pad=4),
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis= {"title":"Temps en minutes"},
        hovermode= 'closest',
    )

    return({"data": data_trace, "layout": layout})