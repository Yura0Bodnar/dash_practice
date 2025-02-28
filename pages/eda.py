import pandas as pd
import plotly.express as px
from dash import dcc, html
import dash
from server import server

# Завантаження датасету
df = pd.read_csv("test_dataset_event.csv")

# Основна інформація про датасет
num_rows, num_cols = df.shape
missing_values = df.isnull().sum().sum()

# Розділення на числові та категорійні змінні
numerical_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns

# Гістограма для першої числової змінної
fig_histogram = px.histogram(df, x=numerical_cols[0], title=f"Розподіл {numerical_cols[0]}")

# Кореляційна матриця
fig_corr = px.imshow(df[numerical_cols].corr(), title="Кореляційна матриця")

# Гістограма для першої категорійної змінної
df_categorical = df[categorical_cols[0]].value_counts().reset_index()
df_categorical.columns = ['category', 'count']  # Перейменовуємо колонки

fig_categorical = px.bar(df_categorical, x="category", y="count",
                         title=f"Розподіл {categorical_cols[0]}")


eda_app = dash.Dash(__name__, server=server, url_base_pathname="/eda/", suppress_callback_exceptions=True)

# Dash layout для відображення аналізу
layout = html.Div([
    html.H1("Exploratory Data Analysis", className="page-title"),
    html.Hr(className="title-line"),

    html.Div([
        html.P(f"📊 Кількість рядків: {num_rows}"),
        html.P(f"📌 Кількість колонок: {num_cols}"),
        html.P(f"⚠️ Пропущені значення: {missing_values}"),
    ], className="eda-summary"),

    html.Div([
        dcc.Graph(figure=fig_histogram),  # Гістограма для числових змінних
        dcc.Graph(figure=fig_corr),  # Кореляційна матриця
        dcc.Graph(figure=fig_categorical),  # Гістограма категорійної змінної
    ], className="eda-graphs"),
], className="page-content")

eda_app.layout = layout
