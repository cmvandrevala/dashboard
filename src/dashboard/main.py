from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd

def create_df():
  df = pd.read_csv("./omnifocus.csv")
  df = df.drop("Context", axis=1)
  df = df.drop("Completion Date", axis=1)
  df = df.drop("Duration", axis=1)
  df = df.drop("Flagged", axis=1)
  df = df.drop("Planned Date", axis=1)
  df = df.drop("Notes", axis=1)
  df = df.drop("Start Date", axis=1)
  df = df.drop("Status", axis=1)
  df = df.drop("Tags", axis=1)
  df = df.drop("Task ID", axis=1)
  return df

def urgent_and_important():
  return [
    html.H3("Urgent & Important (Do)", className="text-center"),
    html.Div(id="q1-tasks", className="p-2 border", children=[
      html.P("Hello")
    ]),
  ]

def urgent_not_important():
  return [
    html.H3("Urgent but Not Important (Delegate)", className="text-center"),
    html.Div(id="q3-tasks", className="p-2 border", children=[
      html.P("Hello")
    ]),
  ]

def important_not_urgent():
  return [
    html.H3("Important but Not Urgent (Schedule)", className="text-center"),
    html.Div(id="q2-tasks", className="p-2 border", children=[
      html.P("Hello")
    ])
  ]

def not_urgent_not_important():
  return [
      html.H3("Not Urgent & Not Important (Eliminate)", className="text-center"),
      html.Div(id="q4-tasks", className="p-2 border", children=[
      html.P("Hello")
    ])
  ]

def create_app():
  app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
  app.layout = dbc.Container([
      html.H1("Eisenhower Matrix", className="text-center my-4"),
      dbc.Row([
          dbc.Col(html.Div(urgent_and_important()), md=6),
          dbc.Col(html.Div(important_not_urgent()), md=6),
      ]),
      dbc.Row([
          dbc.Col(html.Div(urgent_not_important()), md=6),
          dbc.Col(html.Div(not_urgent_not_important()), md=6),
      ])
  ], fluid=True)
  return app


def start():
  df = create_df()
  print(df)
  app = create_app()
  app.run(debug=True)

if __name__ == '__main__':
    start()
