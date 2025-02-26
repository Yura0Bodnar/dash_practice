import dash
from dash import dcc, html, Input, Output, State
from flask import Flask

# Створюємо Flask застосунок
server = Flask(__name__)

# Створюємо Dash застосунок
dash_app = dash.Dash(__name__, server=server, url_base_pathname="/")

# 🔹 **Інтерфейс чату**
dash_app.layout = html.Div([
    html.H1("Чат-бот (макет)"),
    dcc.Input(id="user-input", type="text", placeholder="Напишіть повідомлення", style={"width": "60%"}),
    html.Button("Надіслати", id="send-button", n_clicks=0),
    html.Div(id="chat-response", style={"marginTop": "20px", "fontSize": "18px"})
])

# 🔹 **Dash callback для відображення введеного тексту**
@dash_app.callback(
    Output("chat-response", "children"),
    Input("send-button", "n_clicks"),
    State("user-input", "value")
)
def chat_response(n_clicks, user_input):
    if n_clicks > 0 and user_input:
        return f"Ви написали: {user_input}"
    return "Введіть повідомлення та натисніть 'Надіслати'."

# 🔹 **Запускаємо Flask сервер**
if __name__ == "__main__":
    server.run(debug=True, host="127.0.0.1", port=8000)
