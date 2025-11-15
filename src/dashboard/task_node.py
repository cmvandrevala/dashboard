from anytree import NodeMixin


class TaskNode(NodeMixin):
    def __init__(self, name, parent=None):
      self.name = name
      self.parent = parent
