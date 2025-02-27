from dash import dcc, html, Input, Output, State
import dash
from server import server

# Створюємо локальний Dash застосунок
bot_app = dash.Dash(__name__, server=server, url_base_pathname="/bot/", suppress_callback_exceptions=True)

# 🔹 **Layout сторінки**
layout = html.Div([
    html.H1("Чат-бот", className="page-title"),
    dcc.Input(id="user-input", type="text", placeholder="Напишіть повідомлення", style={"width": "60%"}),
    html.Button("Надіслати", id="send-button", n_clicks=0),
    html.Div(id="chat-response", style={"margin-top": "20px", "font-size": "18px"})
])

# 🔹 **Callback для чату**
@bot_app.callback(
    Output("chat-response", "children"),
    Input("send-button", "n_clicks"),
    State("user-input", "value")
)
def chat_response(n_clicks, user_input):
    if n_clicks > 0 and user_input:
        return f"Ви написали: {user_input}"
    return "Введіть повідомлення та натисніть 'Надіслати'."

bot_app.layout = layout