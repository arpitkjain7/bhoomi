import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd

ss = StandardScaler()


def get_nearest_neighbour(data: dict):
    test_data = pd.DataFrame.from_dict(data)
    X = pd.DataFrame(
        ss.fit_transform(test_data),
        columns=["water_temperature", "tds_level", "ph_level"],
    )
    model = pickle.load(open("artifacts/knnpickle_file", "rb"))
    pred = model.predict(X)
    return pred[0]
