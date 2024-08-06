import os
import pandas as pd

from bck.settings import CLEAN_DIR, FINAL_DIR


ID = "IDRSSD"

POR_COLUMNS = [
    ID,
    "Financial Institution Name",
    "Financial Institution Address",
    "Financial Institution City",
    "Financial Institution State",
    "Financial Institution Zip Code",
    "Financial Institution Filing Type"
]





def get_clean_df_by_year(year="2024"):
    """
    Return the clean df of the balance sheet, income, loan, and location info
    :param year: str
    """
    dfs = list()
    schedules = ["POR", "RI", "RC", "RCK"]
    file_names = [file_name for file_name in os.listdir(CLEAN_DIR) if year in file_name]
    for file_name in file_names:
        for schedule in schedules:
            if schedule in file_name:
                path = os.path.join(CLEAN_DIR, file_name)
                df = pd.read_csv(path, delimiter=",", encoding="utf-8")
                dfs.append(df)

    df_full = dfs[0]
    for df in dfs[1:]:
        df_full = df_full.merge(df, on=ID, how='inner')


    columns = [ID]
    df_full = df_full[columns]

    check = 1
    return df_full


if __name__ == "__main__":
    r = get_clean_df_by_year()

