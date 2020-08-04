import pandas as pd

def preprocess_data(data:dict) -> dict:
    df = pd.DataFrame.from_dict(data)
    
    features = df[df.keys()[1:-1]]
    labels = df[df.keys()[-1]]

    result = {}
    result["features"] = features.to_dict()
    result["labels"] = labels.to_dict()

    print("FEATURES")
    print(features)
    print("LABELS")
    print(labels)

    return result
