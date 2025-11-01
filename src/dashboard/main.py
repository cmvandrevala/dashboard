from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd
import yaml
from datetime import datetime
from zoneinfo import ZoneInfo

def create_raw_df(filepath):
  df = pd.read_csv(filepath)
  df = df.drop("Context", axis=1)
  df = df.drop("Completion Date", axis=1)
  df = df.drop("Duration", axis=1)
  df = df.drop("Planned Date", axis=1)
  df = df.drop("Project", axis=1)
  df = df.drop("Notes", axis=1)
  df = df.drop("Start Date", axis=1)
  df = df.drop("Status", axis=1)
  df = df.drop("Tags", axis=1)
  df = df.drop("Type", axis=1)
  df = df.drop("Task ID", axis=1)
  df['Due Date'] = pd.to_datetime(df['Due Date'])
  print(df)
  return df

def remove_unneeded_entries(df):
  unneeded_entries = []

  with open("./unneeded_entries.yml") as stream:
    try:
        unneeded_entries = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

  return df[df["Name"].isin(unneeded_entries) == False]

def urgent_condition(df):
  return (df['Due Date'].notnull() & (df['Due Date'] <= datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 W")))

def important_condition(df):
  return (df['Flagged'] == True)

def urgent(df):
  return df.where(urgent_condition(df))

def not_urgent(df):
  return df.mask(urgent_condition(df))

def important(df):
  return df.where(important_condition(df))

def not_important(df):
  return df.mask(important_condition(df))

def urgent_and_important(df):
  fdf = urgent(important(df))
  tasks = fdf["Name"].map(lambda x: html.P(x))
  return [
    html.H3("Urgent & Important (Do)", className="text-center"),
    html.Div(id="q1-tasks", className="p-2 border", children=tasks),
  ]

def urgent_not_important(df):
  fdf = urgent(not_important(df))
  tasks = fdf["Name"].map(lambda x: html.P(x))
  return [
    html.H3("Urgent but Not Important (Delegate)", className="text-center"),
    html.Div(id="q3-tasks", className="p-2 border", children=tasks),
  ]

def important_not_urgent(df):
  fdf = not_urgent(important(df))
  tasks = fdf["Name"].map(lambda x: html.P(x))
  return [
    html.H3("Important but Not Urgent (Schedule)", className="text-center"),
    html.Div(id="q2-tasks", className="p-2 border", children=tasks)
  ]

def not_urgent_not_important(df):
  fdf = not_urgent(not_important(df))
  tasks = fdf["Name"].map(lambda x: html.P(x))
  return [
      html.H3("Not Urgent & Not Important (Eliminate)", className="text-center"),
      html.Div(id="q4-tasks", className="p-2 border", children=tasks)
  ]

def create_app(df):
  app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
  app.layout = dbc.Container([
      html.H1("Eisenhower Matrix", className="text-center my-4"),
      dbc.Row([
          dbc.Col(html.Div(urgent_and_important(df)), md=6),
          dbc.Col(html.Div(important_not_urgent(df)), md=6),
      ]),
      dbc.Row([
          dbc.Col(html.Div(urgent_not_important(df)), md=6),
          dbc.Col(html.Div(not_urgent_not_important(df)), md=6),
      ])
  ], fluid=True)
  return app


def start():
  df = create_raw_df("./omnifocus.csv")
  df = remove_unneeded_entries(df)
  app = create_app(df)
  app.run(debug=True)

if __name__ == '__main__':
    start()
