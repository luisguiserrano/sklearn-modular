"""
Copyright Zapata Computing, Inc. All rights reserved.
"""

import json

import pandas as pd
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
        print(data)
        print(data.to_json())
        return data.to_json()

    except Exception as e:
        print(f'Errors: could not load dataset: {e}')

def save_json(result, filename) -> None:
    """
    Saves data as JSON.
    Args:
        result (ditc): of data to save.
        filenames (str): file name to save the data in
            (should have a '.json' extension).
    """
    try:
        with open(filename,'w') as f:
            result["schema"] = "orquestra-v1-data"
            f.write(json.dumps(result, indent=2)) 

    except IOError:
        print(f'Error: Could not open {filename}')

'''
class NumpyArrayEncoder(JSONEncoder):
    """
    Aux classes for decoding NumPy arrays to Python objects.
    Returns:
        A list or a JSONEnconder object.
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
'''