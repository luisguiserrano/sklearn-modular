import pandas as pd

def preprocess_data(data:dict) -> dict:
    df = pd.DataFrame.from_dict(data)

    print("DF")
    print(df)

    print("KEYS")
    print(df.keys())

    features = df[df.keys()[1:-1]]
    labels = df[df.keys()[-1]]

    print("FEATURES")
    print(features)
    print("LABELS")
    print(labels)

    result = {}
    result["features"] = features.to_dict()
    result["labels"] = labels.to_dict()

    return result
