""" Lambdata - a collection of Data Science helper functions"""

# accessing libraries through pipenv
import pandas as pd
import numpy as np
from pandas import DataFrame

FAVORITE_NUMBERS = [3.71, 101, 55, 12, 3.14]

def df_nullsum(df):
    """counts null values"""
    print(df.isnull().sum().sum())
    
    pass

def df_shuffle(df):
    """shuffles df"""
    print(df.sample(frac =1))
    pass


# TODO: helper fuction 
# State abbreviation -> to full name and vise versa
# FL --> Florida, Florida --> FL, etc


def add_state_names_columns(my_df):
    """
    Add a column of corresponding state names to a dataframe.

    Params (my_df) a DataFrame with a column called "abbrev" that has state abbreviations

    Return a the dataframe with an extra column
    """
    new_df = my_df.copy()

    names_map = {"CA": "California", "CO": "Colorado", "CT": "Connecticut"}

    new_df["name"] = new_df["abbrev"].map(names_map)
    
    return my_df


if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())
    
    mapped_df = add_state_names_columns(df)
    print(mapped_df.head())
 