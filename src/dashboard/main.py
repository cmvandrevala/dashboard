import pandas as pd

def start():
  df = pd.read_csv("./omnifocus.csv")
  print(df)

if __name__ == '__main__':
    start()
