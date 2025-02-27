from dash import html
import dash
from server import server

# Створюємо Dash застосунок
upload_app = dash.Dash(__name__, server=server, url_base_pathname="/upload/", suppress_callback_exceptions=True)

# 🔹 **Layout сторінки**
layout = html.Div([
    html.H1("Datasets", className="page-title"),  # Заголовок сторінки
    html.Hr(className="title-line"),

    html.Div([
        html.Button("+ Upload dataset", id="upload-button", n_clicks=0, className="btn-primary"),
    ], className="upload-button-container"),

    # html.Div(id="datasets-container", children="Load dataset", className="upload-message"),

    html.Div([
        html.Div("About_rest_chunks.csv", className="dataset-item"),
        html.Div("CatBoost_chunks.csv", className="dataset-item"),
        html.Div("LightGBM_chunks.csv", className="dataset-item"),
    ], className="dataset-list"),
], className="page-content")

upload_app.layout = layout