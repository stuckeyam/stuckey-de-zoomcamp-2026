#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
from pathlib import Path


# project root is current working directory (where the kernel was started)
# project_root = Path.cwd() #leaving this for reference from jupyterhub notebook
script_dir = Path(__file__).resolve().parent
print(script_dir)
data_path = script_dir / "raw_data" / "green_tripdata_2025-11.parquet"

print(data_path)


df = pd.read_parquet(data_path)


# Create the connection to postgres
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df.to_sql(
    name='green_taxi_trips',
    con=engine,
    if_exists='replace'
)
