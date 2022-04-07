import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine


# MAKE DIFFERENCE BETWEEN PRODUCTION AND DEVELOPMENT ENVIRONMENT
def conn_db(DEV=True):
    if DEV:
        SQL_URI = os.environ.get('SQL_URI')
    else:
        SQL_URI = os.environ.get('SQL_URI_HEROKU')
    if SQL_URI and SQL_URI.startswith("postgres://"):
        SQL_URI = SQL_URI.replace("postgres://", "postgresql://", 1)
    con = create_engine(SQL_URI, echo=False).raw_connection()
    return con



if __name__ == "__main__":
    DEV=False
    sections = ["feedback_book", "buy_hardcover", "report_bug"]
    con = conn_db(DEV)
    query = 'SELECT * FROM "{}";'.format(sections[0])
    df = pd.read_sql(query, con)
    print(df)