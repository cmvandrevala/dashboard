import pandas as pd

def start():
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
  print(df)

if __name__ == '__main__':
    start()
