import pandas as pd

from dashboard.task_node import TaskNode
from anytree import RenderTree

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

    @staticmethod
    def build_tree(df):
      root = TaskNode("ROOT")
      node_tracker = {"ROOT": root}
      for index, row in df.sort_values(by=['Task ID']).iterrows():
        task_id = row["Task ID"]
        if "." in task_id:
          parent_id = ".".join(task_id.split(".")[:-1])
          parent_node = node_tracker[parent_id]
          foo = TaskNode(row["Name"], parent=parent_node)
          node_tracker[task_id] = foo
        else:
          foo = TaskNode(row["Name"], parent=root)
          node_tracker[task_id] = foo
        print(RenderTree(root))

