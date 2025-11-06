from dash import Dash, html, Input, Output
from dash.exceptions import PreventUpdate
from dashboard.data_importer import DataImporter
from dashboard.eisenhower_matrix import EisenhowerMatrix
import dash_bootstrap_components as dbc

class AppCreator:
  eisenhower = None
  app = None

  def __init__(self, df):
    self.eisenhower = EisenhowerMatrix(df)
    self.app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    self.__assign_callbacks(self.app)

  def execute(self):
    self.app.layout = dbc.Container([
        html.H1("Eisenhower Matrix", className="text-center my-4"),
        html.Button('Reload Data', id='reload-data-button', n_clicks=0),
        self.__matrix()
    ], fluid=True)
    return self.app

  def __matrix(self):
    return html.Div([
      dbc.Row([
          dbc.Col(html.Div(self.__urgent_and_important()), md=6),
          dbc.Col(html.Div(self.__important_not_urgent()), md=6),
      ]),
      dbc.Row([
          dbc.Col(html.Div(self.__urgent_not_important()), md=6),
          dbc.Col(html.Div(self.__not_urgent_not_important()), md=6),
      ])
    ], id="eisenhower-matrix")


  def __urgent_and_important(self):
    df = self.eisenhower.urgent_and_important()
    tasks = df["Name"].map(lambda x: html.P(x))
    return [
      html.H3("Urgent & Important (Do)", className="text-center"),
      html.Div(className="p-2 border", children=tasks),
    ]

  def __urgent_not_important(self):
    df = self.eisenhower.urgent_not_important()
    tasks = df["Name"].map(lambda x: html.P(x))
    return [
      html.H3("Urgent but Not Important (Delegate)", className="text-center"),
      html.Div(className="p-2 border", children=tasks),
    ]

  def __important_not_urgent(self):
    df = self.eisenhower.important_not_urgent()
    tasks = df["Name"].map(lambda x: html.P(x))
    return [
      html.H3("Important but Not Urgent (Schedule)", className="text-center"),
      html.Div(className="p-2 border", children=tasks)
    ]

  def __not_urgent_not_important(self):
    df = self.eisenhower.not_urgent_not_important()
    tasks = df["Name"].map(lambda x: html.P(x))
    return [
        html.H3("Not Urgent & Not Important (Eliminate)", className="text-center"),
        html.Div(className="p-2 border", children=tasks)
    ]

  def __assign_callbacks(self, app):
    @app.callback(Output('eisenhower-matrix', 'children'), [Input('reload-data-button', 'n_clicks')])
    def reload_data(n_clicks):
      if n_clicks is None:
        raise PreventUpdate
      else:
        df = DataImporter().import_csv("./Omnifocus.csv")
        self.eisenhower = EisenhowerMatrix(df)
        return self.__matrix()
