from sklearn.datasets import fetch_covtype
import pandas as pd

# Загружаем датасет Covertype — 54 признака
def data_fetch():
    data = fetch_covtype()
    return pd.DataFrame(data.data, columns=data.feature_names)
    