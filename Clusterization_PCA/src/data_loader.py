from datasets import load_dataset
import pandas as pd

def load_data():
    dataset = load_dataset("scikit-learn/covertype")
    return dataset['train'].to_pandas()