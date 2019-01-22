from typing import Optional

import numpy as np
import pandas as pd
from pandas import DataFrame


def reduce(df: DataFrame, inplace: bool = True) -> DataFrame:
    """
    Reduces memory of DataFrame by using the smallest possible data type for each column, copied from
    https://www.kaggle.com/gemartin/load-data-reduce-memory-usage
    :param df: the DataFrame to reduce
    :param inplace: reduce the DataFrame in place or make a copy
    :return: The reduced DataFrame
    """
    if not inplace:
        df = df.copy()

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            col_min = df[col].min()
            col_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if col_min > np.iinfo(np.int8).min and col_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif col_min > np.iinfo(np.int16).min and col_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif col_min > np.iinfo(np.int32).min and col_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif col_min > np.iinfo(np.int64).min and col_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if col_min > np.finfo(np.float16).min and col_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif col_min > np.finfo(np.float32).min and col_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')
    return df


def add_date_fields(df: DataFrame, date_field: str, prefix: Optional[str] = None, inplace: bool = True) -> DataFrame:
    """
    Adds extra date and time fields to a DataFrame with a date column
    :param df: The DataFrame to add date fields to
    :param date_field: The name of the date column in the DataFrame
    :param prefix: An optional prefix to add to the appended columns
    :param inplace: Add in place or make a copy of the DataFrame
    :return: The DataFrame with date fields appended
    """
    if not inplace:
        df = df.copy()

    if not prefix:
        prefix = date_field

    datetimes = pd.to_datetime(df[date_field], infer_datetime_format=True)
    fields = ['year', 'month', 'day', 'hour', 'minute', 'dayofyear', 'weekofyear', 'week', 'dayofweek', 'weekday',
              'quarter']
    for field in fields:
        field_name = '{}_{}'.format(prefix, field)
        df[field_name] = getattr(datetimes.dt, field)
    return df
