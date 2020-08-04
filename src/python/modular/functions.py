import pandas as pd

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
