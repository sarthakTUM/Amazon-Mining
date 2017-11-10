"""
Demo script to load data in Python IDE.
"""
from src.data.json_loader import JSONLoader


def load_data():
    """
    Follow the steps:
    1. get the loader object
    2. load the file by supplying the file_name, using the loader object.
    :return:
    """
    loader = JSONLoader()
    df = loader.load_data('/media/sarthak/HDD/TUM/courses/sem 3/practical DM/datasets/meta_Electronics.json.gz')

    # prints the top rows of dataframe
    print(df.head())

    # prints the bottom rows of dataframe
    print(df.tail())


if __name__ == '__main__':
    load_data()
