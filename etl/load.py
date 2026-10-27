#load
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


DB_NAME =os.getenv("DB_NAME")
DB_USER =os.getenv("DB_USER")
DB_PASSWORD =os.getenv("DB_PASSWORD")
DB_PORT =os.getenv("DB_PORT")
DB_HOST =os.getenv("DB_HOST")


def load_to_postgres(df,table_name):
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    df.to_sql(table_name,
              engine,
              if_exists ="replace",
              index = False
              )
    print("Data loaded to postgresql successfully")
