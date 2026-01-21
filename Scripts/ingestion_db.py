import pandas as pd
import os
from sqlalchemy import create_engine, text

# CONNECT TO MYSQL (NO DATABASE) ---------------
engine_without_db = create_engine(
    "mysql+mysqlconnector://root:Shubham%40123@localhost:3306/"
)

# CREATE DATABASE IF NOT EXISTS ----------------
with engine_without_db.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS inventory"))
    print("Database 'inventory' is ready.")

# CONNECT TO THE DATABASE ----------------------
engine = create_engine(
    "mysql+mysqlconnector://root:Shubham%40123@localhost:3306/inventory"
)

# FUNCTION: INGEST DATA ------------------------
def ingest_db(file_path, table_name, engine, chunksize=100000):
    first_chunk = True

    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        with engine.begin() as conn:
            chunk.to_sql(
                table_name,
                con=conn,
                if_exists="replace" if first_chunk else "append",
                index=False
            )
        first_chunk = False


# FUNCTION: LOAD CSV FILES ---------------------
def load_raw_data():
    data_path = r"C:\Users\LENOVO\Downloads\data\data"

    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            try:
                file_path = os.path.join(data_path, file)
                print(f"Ingesting {file} into database...")
                ingest_db(file_path, file[:-4], engine)

            except Exception as e:
                print(f"Error ingesting {file}: {e}")

    print("-------------- INGESTION COMPLETE --------------")



# ENTRY POINT ----------------------------------
if __name__ == "__main__":
    load_raw_data()
