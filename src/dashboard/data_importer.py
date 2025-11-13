import pandas as pd
import yaml

from dashboard.data_cleaner import DataCleaner

class DataImporter:
    df = None

    def import_csv(self, filepath):
      self.df = pd.read_csv(filepath)
      self.df = DataCleaner.drop_unused_columns(self.df);
      self.df = DataCleaner.format_due_date(self.df);
      self.__remove_unneeded_entries();
      return self.df

    def __remove_unneeded_entries(self):
      unneeded_entries = []

      with open("./unneeded_entries.yml") as stream:
        try:
            unneeded_entries = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

      self.df = self.df[self.df["Name"].isin(unneeded_entries) == False]
