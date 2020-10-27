""" Lambdata - a collection of Data Science helper functions"""

# accessing libraries through pipenv
import pandas as pd
import numpy as np


FAVORITE_NUMBERS = [3.71, 101, 55, 12, 3.14]

def df_nullsum(df):
    """counts null values"""
    df.isnull().sum().sum()
    # TODO - implement df_cleaner
    pass

def df_shuffle(df):
    """shuffles df"""
    df.sample(frac =1)
    pass