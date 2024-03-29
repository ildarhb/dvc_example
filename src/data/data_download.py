import os

from sklearn import datasets
import pandas as pd


if __name__ == "__main__":  
    dataset = datasets.load_diabetes()
    features = pd.DataFrame(data=dataset.data, 
                            columns=["feat%s" % x for x in range(dataset.data.shape[1])])
    target = pd.DataFrame(data=dataset.target, columns=["target"])

    features.to_csv("./data/initial_data/initial_data.csv")
    target.to_csv("./data/initial_data/target.csv")