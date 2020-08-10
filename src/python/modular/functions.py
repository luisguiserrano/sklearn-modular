import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
import numpy as np
from pkg_resources import resource_string

def read_dataset(filename):
    try:
        data = resource_string(__name__, filename)
        data_utf8 = str(data, 'utf-8')
        data_list = data_utf8.splitlines()
        names = np.asarray(data_list[0].split(','))
        values = np.asarray([dt.split(',') for dt in data_list[1:]])
        data = pd.DataFrame(values, columns=names)
        return data
        #result = {}
        #result["data"] = data.to_dict()
        #return result

    except Exception as e:
        print(f'Errors: could not load dataset: {e}')

def preprocess_data(data:dict) -> dict:
    #df = pd.DataFrame.from_dict(data)['data']
    features = data[data.keys()[:-1]]
    labels = data[data.keys()[-1]]

    return features, labels
    #result = {}
    #result["features"] = features.to_dict()
    #result["labels"] = labels
    #return result

def train_perceptron(features, labels):
    f = pd.DataFrame.from_dict(features)
    l = pd.DataFrame.from_dict([labels]).transpose()
    model = LogisticRegression()
    model.fit(f, l)
    return model

def make_predictions(model, features):
    predictions = model.predict(features)
    return predictions

def score_model(model, features, labels):
    score = model.score(features, labels)
    return score

raw_data = read_dataset('datasets/data.csv')
data = preprocess_data(raw_data)
features = data["features"]
labels = data["labels"]

train_perceptron(features, labels)