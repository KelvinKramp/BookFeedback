import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()


# MAKE DIFFERENCE BETWEEN PRODUCTION AND DEVELOPMENT ENVIRONMENT
def conn_db():
    from sqlalchemy import create_engine
    SQL_URI = os.environ.get('DATABASE_URL')
    if SQL_URI and SQL_URI.startswith("postgres://"):
        SQL_URI = SQL_URI.replace("postgres://", "postgresql://", 1)
    con = create_engine(SQL_URI, echo=True).raw_connection()
    return con


def get_from_db(section):
    con = conn_db()

    # DIFFERENT TABLE SELECTIONS
    df = pd.read_sql('SELECT * FROM "{}";'.format(section), con)
    df.to_csv("feedback.csv")
    return


if __name__ == "__main__":
    sections = ["feedback_book", "buy_hardcover", "report_bug"]
    df = get_from_db()
    print(df)