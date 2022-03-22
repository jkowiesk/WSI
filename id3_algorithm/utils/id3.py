import numpy as np
from utils.node import Node


class ID3:
    def __init__(self, max_depth=100):
        self._root = None
        self.max_depth = max_depth

    def build_tree(self, X, Y):
        rows = [(x, y) for x, y in zip(X, Y)]
        self._root = self.build_tree_recurr(rows, None)

    def build_tree_recurr(self, rows, feature_value, depth=0):
        features_num = len(rows[0][0])
        children = []
        classes = self._get_classes(rows)

        rows_entropy = self._get_entropy(len(rows), classes)

        if depth < self.max_depth and len(classes) > 1:
            best_feature = self._get_best_feature(rows, features_num, rows_entropy)
            unique_best_fvs = np.unique([row[0][best_feature["feature_index"]] for row in rows])
            for unique_best_fv in unique_best_fvs:
                new_rows = self._get_new_rows(rows, best_feature["feature_index"], unique_best_fv)
                new_rows = [(np.delete(row[0], best_feature["feature_index"]), row[1]) for row in new_rows]
                children.append(self.build_tree_recurr(new_rows, unique_best_fv, depth+1))

            return Node(best_feature["feature_index"], children,
                        best_feature["info_gain"], feature_value, classes)
        return Node(feature_value=feature_value, classes=classes)

    def predict(self, row_x, node=None):
        """
        Method which classifies given features (row_x)
        """
        if node is None:
            node = self._root

        if node.children:
            for child in node.children:
                if child.feature_value == row_x[node.feature_index]:
                    if len(child.classes) == 1:
                        return list(child.classes.keys())[0]
                    else:
                        row_x = np.delete(row_x, node.feature_index)
                        return self.predict(row_x, child)
        return max(node.classes, key=node.classes.get)

    def _get_best_feature(self, rows, features_num, rows_entropy):
        best_feature = dict()
        best_feature["info_gain"] = float('-inf')
        for feature_index in range(features_num):
            info_gain = self._get_inf_gain(rows, feature_index, rows_entropy)
            if info_gain > best_feature["info_gain"]:
                best_feature["info_gain"] = info_gain
                best_feature["feature_index"] = feature_index
        return best_feature

    def _get_new_rows(self, rows, feature_index, unique_feature):
        new_rows = list()

        for row in rows:
            if row[0][feature_index] == unique_feature:
                new_rows.append(row)
        return new_rows

    def _get_classes(self, rows):
        classes = [row[1] for row in rows]
        unique_cvs_list = np.unique(classes)
        unique_cvs = dict()

        for unique_cv in unique_cvs_list:
            unique_cvs[unique_cv] = 0

        for class_value in classes:
            unique_cvs[class_value] += 1

        return unique_cvs

    def _get_inf_gain(self, rows, feature_index, rows_entropy):
        unique_features = np.unique([row[0][feature_index] for row in rows])
        inf = 0
        rows_num = len(rows)
        for unique_feature in unique_features:
            new_rows = self._get_new_rows(rows, feature_index, unique_feature)
            unique_cvs = self._get_classes(new_rows)
            inf += len(new_rows) / rows_num * self._get_entropy(len(new_rows), unique_cvs)
        return rows_entropy - inf

    def _get_entropy(self, rows_num, unique_cvs):
        entropy = 0

        for unique_cv in unique_cvs.values():
            f = unique_cv / rows_num
            entropy -= f * np.log(f)

        return entropy

    def get_root(self):
        return self._root
