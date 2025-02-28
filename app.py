import dash
from dash import dcc, html, Input, Output
from flask import Flask
from pages.bot import layout as bot_layout
from pages.predict import layout as predict_layout
from pages.dataset import layout as upload_layout
from pages.eda import layout as eda_layout

# Створюємо Flask сервер
server = Flask(__name__)

# Створюємо Dash застосунок
dash_app = dash.Dash(__name__, server=server, url_base_pathname="/", suppress_callback_exceptions=True,
                     external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"])

# 🔹 Sidebar (бокове меню)
sidebar = html.Div(
    [
        html.H2("Меню", className="sidebar-header"),
        dcc.Link("🔮 Predict", href="/predict", className="sidebar-link"),
        dcc.Link("🤖 Bot", href="/bot", className="sidebar-link"),
        dcc.Link("📂 Upload", href="/upload", className="sidebar-link"),
        dcc.Link("📊 EDA", href="/eda", className="sidebar-link"),
    ],
    className="sidebar"
)

# 🔹 Основний layout
dash_app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    sidebar,
    html.Div(id="page-content", className="content")  # Контентна частина
])

# 🔹 Callback для перемикання сторінок
@dash_app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/bot":
        return bot_layout
    elif pathname == "/upload":
        return upload_layout
    elif pathname == "/eda":
        return eda_layout
    return bot_layout
# 🔹 Запускаємо сервер
if __name__ == "__main__":
    server.run(debug=True, host="127.0.0.1", port=8000)
