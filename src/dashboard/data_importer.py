import pandas as pd
import yaml


class DataImporter:
    df = None

    def import_csv(self, filepath):
      self.df = pd.read_csv(filepath)
      self.__drop_unused_columns();
      self.__remove_unneeded_entries();
      return self.df

    def __drop_unused_columns(self):
      self.df = self.df.drop("Context", axis=1)
      self.df = self.df.drop("Completion Date", axis=1)
      self.df = self.df.drop("Duration", axis=1)
      self.df = self.df.drop("Planned Date", axis=1)
      self.df = self.df.drop("Project", axis=1)
      self.df = self.df.drop("Notes", axis=1)
      self.df = self.df.drop("Start Date", axis=1)
      self.df = self.df.drop("Status", axis=1)
      self.df = self.df.drop("Tags", axis=1)
      self.df = self.df.drop("Type", axis=1)
      self.df = self.df.drop("Task ID", axis=1)
      self.df['Due Date'] = pd.to_datetime(self.df['Due Date'])

    def __remove_unneeded_entries(self):
      unneeded_entries = []

      with open("./unneeded_entries.yml") as stream:
        try:
            unneeded_entries = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

      self.df = self.df[self.df["Name"].isin(unneeded_entries) == False]
