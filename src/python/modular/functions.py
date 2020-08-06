import pandas as pd
import sklearn
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
        result = {}
        result["data"] = data.to_dict()
        #print(result.keys())
        #print(result['data'].keys())
        #print("=======")
        #print(result['data'][''])
        #print("=======")
        #print(result['data']['x_1'])
        #print("=======")
        #print(result['data']['x_2'])
        #print("=======")
        #print(result['data']['y'])
        return result

    except Exception as e:
        print(f'Errors: could not load dataset: {e}')

def preprocess_data(data:dict) -> dict:
    #print("PREPROCESSING DATA")
    df = pd.DataFrame.from_dict(data)['data']

    #print("DF")
    #print(type(df))
    #print(df)

    #print("KEYS")
    #print(type(df.keys()))
    #print(df.keys())

    features = df[df.keys()[:-1]]
    labels = df[df.keys()[-1]]

    #print("FEATURES")
    #print(type(features))
    #print(features)
    #print("LABELS")
    #print(type(labels))
    #print(labels)

    result = {}
    result["features"] = features.to_dict()
    result["labels"] = labels

    #print("RESULTS")
    print(result.keys())
    print(result)

    return result

def train_model(features, labels):
    model = sklearn.linear_model.LogisticRegression()
    model.fit(features, labels)
    return model

def make_predictions(model, features):
    predictions = model.predict(features)
    return predictions

def score_model(model, features, labels):
    score = model.score(features, labels)
    return score

#print("1")
#data = read_dataset('datasets/data.csv')
#print("2")
#preprocess_data(data)