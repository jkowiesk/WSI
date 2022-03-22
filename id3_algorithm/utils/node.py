class Node:
    def __init__(self, feature_index=None, children=None,
                 inf_gain=None, feature_value=None, classes=None):
        self.feature_index = feature_index
        self.children = children
        self.inf_gain = inf_gain
        self.feature_value = feature_value
        self.classes = classes