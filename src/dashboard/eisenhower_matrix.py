import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

class EisenhowerMatrix:
    df = None

    def __init__(self, df):
      self.df = df

    def urgent_and_important(self):
      return self.__sort_by_due_date(self.__urgent(self.__important(self.df)))

    def urgent_not_important(self):
      return self.__sort_by_due_date(self.__urgent(self.__not_important(self.df)))

    def important_not_urgent(self):
      return self.__sort_by_due_date(self.__not_urgent(self.__important(self.df)))

    def not_urgent_not_important(self):
      return self.__sort_by_due_date(self.__not_urgent(self.__not_important(self.df)))

    def __urgent_condition(self, df):
      return (df['Due Date'].notnull() & (df['Due Date'] <= datetime.now(ZoneInfo("UTC")) + pd.to_timedelta("1 W")))

    def __important_condition(self, df):
      return (df['Flagged'] == True)

    def __urgent(self, df):
      return df.loc[self.__urgent_condition(df)]

    def __not_urgent(self, df):
      return df.mask(self.__urgent_condition(df))

    def __important(self, df):
      return df.loc[self.__important_condition(df)]

    def __not_important(self, df):
      return df.mask(self.__important_condition(df))

    def __sort_by_due_date(self, df):
      return df.sort_values(by=['Due Date'])
