import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

script_dir = Path(__file__).resolve().parent
data_path = script_dir.parent / "raw_data" / "taxi_zone_lookup.csv"
# print(script_dir)
# print(data_path)

zone_csv_file = '../raw_data/taxi_zone_lookup.csv'
df = pd.read_csv(zone_csv_file)

# Create the connection to postgres
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df.to_sql(
    name='zones',
    con=engine,
    if_exists='replace'
)