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
        return data

    except Exception as e:
        print(f'Errors: could not load dataset: {e}')
