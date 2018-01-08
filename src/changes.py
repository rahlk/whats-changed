from __future__ import division

import pandas as pd
from pdb import set_trace
from stats import hedges_g, a12
from data.GetData import get_all_projects

if __name__ == "__main__":
    all = get_all_projects()
    top_changes = []
    for prj_name, prj_data in all.iteritems():
        change_all_datasets = []
        for one, two in zip(prj_data.data[:-1], prj_data.data[1:]):
            one = pd.read_csv(one).dropna().reset_index()
            two = pd.read_csv(two).dropna().reset_index()
            attributes = one.columns
            change = []
            for attr in attributes[2:-1]:
                change.append(a12(one[attr], two[attr]))
            change_all_datasets.append(change)
        change_all_datasets = pd.DataFrame(
            change_all_datasets, columns=attributes[2:-1])
        features = change_all_datasets.median().sort_values(ascending=False).index.tolist()
        top_changes.append([prj_name] + features)
    top_changes = pd.DataFrame(top_changes, columns=[
                               "Name"] + range(len(attributes[2:-1])))
    set_trace()
