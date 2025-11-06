from dashboard.app_creator import AppCreator
from dashboard.data_importer import DataImporter

global_df = None

def start():
  global global_df
  global_df = DataImporter().import_csv("./Omnifocus.csv")
  AppCreator(global_df).execute().run(debug=True)

if __name__ == '__main__':
    start()
