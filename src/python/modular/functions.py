import pandas as pd
import sklearn

def preprocess_data(data:dict) -> dict:
    df = pd.DataFrame.from_dict(data)['data']

    print("DF")
    print(type(df))
    print(df)

    print("KEYS")
    print(type(df.keys()))
    print(df.keys())

    features = df[df.keys()[:-1]]
    labels = df[df.keys()[-1]]

    print("FEATURES")
    print(type(features))
    print(features)
    print("LABELS")
    print(type(labels))
    print(labels)

    result = {}
    result["features"] = features.to_dict()
    result["labels"] = labels

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
