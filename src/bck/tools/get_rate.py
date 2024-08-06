import os
import pandas as pd

from bck.settings import CLEAN_DIR, FINAL_DIR
from bck.tools.schedule_mappings import (
    ID_1,
    ID_2,
    ID_MAPPING,
    NAME,
    SCHED,
    MAPPING,
    POR_INFO,
    RI_INFO,
    RCK_INFO
)


SCHED_INFOS = [POR_INFO, RI_INFO, RCK_INFO]
KEEP_COLUMNS = [ID_1]


for sched_info in SCHED_INFOS:
    loan_mapping = sched_info[MAPPING]
    for loan_type in loan_mapping:
        mdrm = loan_mapping[loan_type]
        KEEP_COLUMNS.append(mdrm)


def get_clean_df_by_year(year="2024", quarter="q1"):
    """
    Return the clean df of the balance sheet, income, loan, and location info
    :param year: str
    :param quarter: str
    """
    dfs = list()
    schedules = ["POR", "RI", "RCK"]
    file_names = [f"call_{year}{quarter}_ {sched} .csv" for sched in schedules]
    for file_name in file_names:
        path = os.path.join(CLEAN_DIR, file_name)
        if os.path.isfile(path):
                df = pd.read_csv(path, delimiter=",", encoding="utf-8")
                dfs.append(df)

    df_final = dfs[0]
    for df in dfs[1:]:
        df_final = df_final.merge(df, on=ID_1, how='inner')

    df_final = df_final[KEEP_COLUMNS]
    df_final = df_final.loc[:, ~df_final.columns.duplicated()]  # remove duplicate columns
    df_final.rename(columns=ID_MAPPING, inplace=True)

    for sched_info in SCHED_INFOS:
        loan_mapping = sched_info[MAPPING]
        if sched_info[SCHED] == "POR":
            inverted = {loan_mapping[key]: key for key in loan_mapping}
        else:
            inverted = {loan_mapping[key]: f"{sched_info[NAME]} - {key}" for key in loan_mapping}
        df_final.rename(columns=inverted, inplace=True)

    for loan in RI_INFO[MAPPING]:
        try:
            df_final[f"Rate - {loan}"] = (4.0 * df_final[f"{RI_INFO[NAME]} - {loan}"]) / df_final[f"{RCK_INFO[NAME]} - {loan}"]
        except Exception as e:
            pass

    target = "Rate - Single Family Home Loans"
    df_sorted_ascending = df_final.sort_values(by=target, ascending=True)
    df_sorted_descending = df_final.sort_values(by=target, ascending=False)


    check = 1
    return df_final


if __name__ == "__main__":
    r = get_clean_df_by_year()

