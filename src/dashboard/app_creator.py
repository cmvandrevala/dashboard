from dash import Dash, html
import dash_bootstrap_components as dbc

class AppCreator:
  eisenhower = None

  def __init__(self, eisenhower):
    self.eisenhower = eisenhower

  def execute(self):
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dbc.Container([
        html.H1("Eisenhower Matrix", className="text-center my-4"),
        dbc.Row([
            dbc.Col(html.Div(self.__urgent_and_important()), md=6),
            dbc.Col(html.Div(self.__important_not_urgent()), md=6),
        ]),
        dbc.Row([
            dbc.Col(html.Div(self.__urgent_not_important()), md=6),
            dbc.Col(html.Div(self.__not_urgent_not_important()), md=6),
        ])
    ], fluid=True)
    return app

  def __urgent_and_important(self):
    df = self.eisenhower.urgent_and_important()
    tasks = df["Name"].map(lambda x: html.P(x))
    return [
      html.H3("Urgent & Important (Do)", className="text-center"),
      html.Div(id="q1-tasks", className="p-2 border", children=tasks),
    ]

  def __urgent_not_important(self):
    df = self.eisenhower.urgent_not_important()
    tasks = df["Name"].map(lambda x: html.P(x))
    return [
      html.H3("Urgent but Not Important (Delegate)", className="text-center"),
      html.Div(id="q3-tasks", className="p-2 border", children=tasks),
    ]

  def __important_not_urgent(self):
    df = self.eisenhower.important_not_urgent()
    tasks = df["Name"].map(lambda x: html.P(x))
    return [
      html.H3("Important but Not Urgent (Schedule)", className="text-center"),
      html.Div(id="q2-tasks", className="p-2 border", children=tasks)
    ]

  def __not_urgent_not_important(self):
    df = self.eisenhower.not_urgent_not_important()
    tasks = df["Name"].map(lambda x: html.P(x))
    return [
        html.H3("Not Urgent & Not Important (Eliminate)", className="text-center"),
        html.Div(id="q4-tasks", className="p-2 border", children=tasks)
    ]

