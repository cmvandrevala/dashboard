import pandas as pd

class DataCleaner:

    @staticmethod
    def drop_unused_columns(df):
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
      return df

    @staticmethod
    def format_due_date(df):
      df['Due Date'] = pd.to_datetime(df['Due Date'])
      return df
