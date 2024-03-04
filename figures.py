import plotly.express as px
import pandas as pd
import numpy as np
df = pd.read_csv("HISTORICO-MLG-2023.CSV")
def line_chart(df):
    """
    Sample Plotly Line Chart
    """
    fig = px.line(df, x="CLICOD", y="TOTALDEUDA", title="Total Debt Over CLICOD")
    return fig

def bar_chart(df):
    """
    Sample Plotly Bar Chart
    """
    fig = px.bar(df, x="PROVINCIA", y="TOTALDEUDA", title="Total Debt by Province")
    return fig

def scatter_plot(df):
    """
    Sample Plotly Scatter Plot
    """
    fig = px.scatter(df, x="KWH-1", y="FAC-1", title="Scatter Plot")
    return fig

def box_plot(df):
    """
    Sample Plotly Box Plot
    """
    fig = px.box(df, x="KWH-2", y="FAC-2", title="Box Plot")
    return fig

def histogram(df):
    """
    Sample Plotly Histogram
    """
    fig = px.histogram(df, x="FAC-3", title="Histogram")
    return fig

def pie_chart(df):
    """
    Sample Plotly Pie Chart
    """
    fig = px.pie(df, values="TOTALDEUDA", names="PROVINCIA", title="Total Debt by Province")
    return fig

