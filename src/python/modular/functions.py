import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
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
    #f = pd.DataFrame.from_dict(features)
    #l = pd.DataFrame.from_dict([labels]).transpose()
    model = LogisticRegression()
    model.fit(features, labels)
    return model

def train_decision_tree(features, labels):
    model = DecisionTreeClassifier()
    model.fit(features, labels)
    return model

def train_svm(features, labels):
    model = SVC()
    model.fit(features, labels)
    return model

def train_model(features, labels, model_name="perceptron"):
    if model_name == "perceptron":
        return train_perceptron(features, labels)
    if model_name == "decisiontree":
        return train_decision_tree(features, labels)
    elif model_name == "svm":
        return train_svm(features, labels)
    else:
        return train_perceptron(features, labels)

def make_predictions(model, features, labels):
    predictions = model.predict(features)
    result = {}
    result['x_1'] = features['x_1']
    result['x_2'] = features['x_2']
    result['y'] = labels
    result['y_pred'] = predictions
    return result

def score_model(model, features, labels):
    score = model.score(features, labels)
    return score

#data = read_dataset('datasets/data.csv')
#features, labels = preprocess_data(data)
#model = train_model(features, labels, 'decisiontree')
#predictions = make_predictions(model, features, labels)
#score = score_model(model, features, labels)
#print(predictions)
#print(score)