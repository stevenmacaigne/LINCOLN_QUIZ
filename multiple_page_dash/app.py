import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv("data.csv")

app = dash.Dash(__name__)

server = app.server
app.config.suppress_callback_exceptions = True

# if __name__ == '__main__':
#      app.run_server(debug=True)