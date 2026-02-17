"""
Creates a function that fetches Statcast data to use for analysis
"""
import os
import pandas as pd
import pybaseball.statcast as pyb

def get_statcast_data(start_date, end_date, filename="statcast_data.parquet"):
    """
    Fetches Statcast data if the file doesn't exist; otherwise, loads it from disk.
    """
    ## does the data already exist?
    if os.path.exists(filename):
        return pd.read_parquet(filename)
    else:
        df = pyb(start_dt=start_date, end_dt=end_date)
        df.to_parquet(filename, index=False)
        return df

