from dash import Dash, html
import dash_bootstrap_components as dbc
from dashboard.data_importer import DataImporter
from dashboard.eisenhower_matrix import EisenhowerMatrix

def urgent_and_important(eisenhower):
  df = eisenhower.urgent_and_important()
  tasks = df["Name"].map(lambda x: html.P(x))
  return [
    html.H3("Urgent & Important (Do)", className="text-center"),
    html.Div(id="q1-tasks", className="p-2 border", children=tasks),
  ]

def urgent_not_important(eisenhower):
  df = eisenhower.urgent_not_important()
  tasks = df["Name"].map(lambda x: html.P(x))
  return [
    html.H3("Urgent but Not Important (Delegate)", className="text-center"),
    html.Div(id="q3-tasks", className="p-2 border", children=tasks),
  ]

def important_not_urgent(eisenhower):
  df = eisenhower.important_not_urgent()
  tasks = df["Name"].map(lambda x: html.P(x))
  return [
    html.H3("Important but Not Urgent (Schedule)", className="text-center"),
    html.Div(id="q2-tasks", className="p-2 border", children=tasks)
  ]

def not_urgent_not_important(eisenhower):
  df = eisenhower.not_urgent_not_important()
  tasks = df["Name"].map(lambda x: html.P(x))
  return [
      html.H3("Not Urgent & Not Important (Eliminate)", className="text-center"),
      html.Div(id="q4-tasks", className="p-2 border", children=tasks)
  ]

def create_app(eisenhower):
  app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
  app.layout = dbc.Container([
      html.H1("Eisenhower Matrix", className="text-center my-4"),
      dbc.Row([
          dbc.Col(html.Div(urgent_and_important(eisenhower)), md=6),
          dbc.Col(html.Div(important_not_urgent(eisenhower)), md=6),
      ]),
      dbc.Row([
          dbc.Col(html.Div(urgent_not_important(eisenhower)), md=6),
          dbc.Col(html.Div(not_urgent_not_important(eisenhower)), md=6),
      ])
  ], fluid=True)
  return app


def start():
  df = DataImporter().import_csv("./omnifocus.csv")
  eisenhower = EisenhowerMatrix(df)
  create_app(eisenhower).run(debug=True)

if __name__ == '__main__':
    start()
