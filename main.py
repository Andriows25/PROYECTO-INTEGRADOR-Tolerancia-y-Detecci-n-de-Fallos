from flask import Flask, render_template
from dash import Dash, html, dcc
from figures import line_chart, bar_chart, scatter_plot, box_plot, histogram, pie_chart
import pandas as pd
df = pd.read_csv("HISTORICO-MLG-2023.csv")
# Initialize Flask server:
server = Flask(__name__, template_folder = "templates")

# Define Routes:
@server.route("/")
def home():
    """
        Redirecting to home page.
    """
    return render_template("home.html")

# Dash Apps:
app1 = Dash(__name__, server = server, url_base_pathname = "/sampleDashApp1/", assets_folder = "assets")
app1.layout = html.Div([
    html.H1("Sample Dash App"),
    html.P("This is a simple Dash app running on a Flask server."),
    html.H2("Sample Line Chart"),
    dcc.Graph(figure=line_chart(df)),
    html.H2("Sample Bar Chart"),
    dcc.Graph(figure=bar_chart(df)),
    html.H2("Sample Scatter Plot"),
    dcc.Graph(figure=scatter_plot(df)),
    html.H2("Sample Box Plot"),
    dcc.Graph(figure=box_plot(df)),
    html.H2("Sample Histogram"),
    dcc.Graph(figure=histogram(df)),
    html.H2("Sample Pie Chart"),
    dcc.Graph(figure=pie_chart(df))
])


# Run the App:
if __name__ == "__main__":
    server.run(host = "0.0.0.0", port = 5000, debug = True) # Set debug to False during production