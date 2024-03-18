import os

import pandas as pd

def fillna(dataset: pd.DataFrame) -> pd.DataFrame:

    prepare_dataset = dataset.copy()
    for i, column in enumerate(dataset.columns):
        if i % 2 == 0:
            prepare_dataset[column] = prepare_dataset[column] - 1
        else:
            prepare_dataset[column] = prepare_dataset[column] - 2
    
    return prepare_dataset

if __name__ == "__main__":
    dataset = pd.read_csv("./data/initial_data/initial_data.csv")
    prepared_dataset = fillna(dataset=dataset)
    prepared_dataset.to_csv("./data/prepared_data/prepared_data.csv")