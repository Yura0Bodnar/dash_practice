import dash
from dash import dcc, html, Input, Output
from flask import Flask
from pages.bot_page import layout as bot_layout
from pages.predict_page import layout as predict_layout

# Створюємо Flask сервер
server = Flask(__name__)

# Створюємо Dash застосунок
dash_app = dash.Dash(__name__, server=server, url_base_pathname="/", suppress_callback_exceptions=True)

# 🔹 Sidebar (бокове меню)
sidebar = html.Div(
    [
        html.H2("Меню", className="sidebar-header"),
        html.Hr(),
        dcc.Link("🔮 Predict", href="/predict", className="sidebar-link"),
        dcc.Link("🤖 Bot", href="/bot", className="sidebar-link"),
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
        return bot_layout  # Використовуємо layout з `bot_page.py`
    return predict_layout  # За замовчуванням відкривається "Predict"

# 🔹 Запускаємо сервер
if __name__ == "__main__":
    server.run(debug=True, host="127.0.0.1", port=8000)
