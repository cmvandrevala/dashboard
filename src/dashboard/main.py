from dashboard.app_creator import AppCreator
from dashboard.data_importer import DataImporter
from dashboard.eisenhower_matrix import EisenhowerMatrix

def start():
  df = DataImporter().import_csv("./omnifocus.csv")
  eisenhower = EisenhowerMatrix(df)
  AppCreator(eisenhower).execute().run(debug=True)

if __name__ == '__main__':
    start()
