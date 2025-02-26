from dash import dcc, html, Input, Output, State
import lightgbm as lgb
import numpy as np
from server import server
import dash

# Створюємо локальний Dash застосунок
predict_app = dash.Dash(__name__, server=server, url_base_pathname="/predict/", suppress_callback_exceptions=True)

# Фейкові дані для навчання
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([10, 20, 30, 40, 50])
model = lgb.LGBMRegressor()
model.fit(X_train, y_train)

# 🔹 **Layout сторінки без inline-стилів**
layout = html.Div([
    html.H1("Прогнозування значень", className="page-title"),
    dcc.Input(id="input-value", type="number", placeholder="Введіть число", className="input-field"),
    html.Button("Прогнозувати", id="predict-button", n_clicks=0, className="btn-primary"),
    html.Div(id="output-prediction", className="output-box")
])

# 🔹 **Callback для прогнозування**
@predict_app.callback(
    Output("output-prediction", "children"),
    Input("predict-button", "n_clicks"),
    State("input-value", "value")
)
def predict(n_clicks, value):
    if n_clicks > 0 and value is not None:
        prediction = model.predict(np.array([[value]]))
        return f"Прогнозоване значення: {prediction[0]:.2f}"
    return ""

predict_app.layout = layout