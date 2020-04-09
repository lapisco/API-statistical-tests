
def loading_file(data):

    """
    data:

    """
    
    import pandas as pd
    # import numpy as np
    # from pandas import DataFrame

    # data_frame = pd.read_csv(data + '.csv', index_col=False)
    data_frame = pd.read_csv(data, index_col=False)
    data_frame = data_frame.drop(data_frame.columns[0], axis=1)

    return data_frame


def transform2array(data):
    """
    data: 

    """
    import numpy as np

    array = np.asarray(data, np.float)

    return array


def save_dataframe(file_name, data):

    """
    file_name: 
    data: 

    """

    from pandas import DataFrame

    df = DataFrame(data)
    df.to_csv(str(file_name) + '.csv')


def save_results(data):
    """
    data:

    """

    with open('results.txt', 'w') as f:
        f.write('{:.5f}'.format(data))
        f.write('\n')