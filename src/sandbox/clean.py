import os
import pandas as pd
import numpy as np

raw_dir = os.path.join("..", "data", "raw")
clean_dir = os.path.join("..", "data", "clean")


raw_dict = dict()
for call_year_quarter in os.listdir(raw_dir):
    raw_dict[call_year_quarter] = list()
print(raw_dict)


count = 0
for call_year_quarter in raw_dict:
    raw_dict[call_year_quarter] = list(os.listdir(os.path.join(raw_dir, call_year_quarter)))
print(raw_dict[call_year_quarter])


def read_text(path):
    with open(path, encoding="utf-8") as f:
        lines = list(f.readlines())

    index = 0
    data = list()
    columns = list()
    for i, lines in enumerate(lines):
        parts = lines.split("\t")[:-1]  # remove empyt newline at end

        if i == 0:  # mdrms
            for p in parts:
                columns.append(p.replace('"', ''))
                data.append(list())

        elif i == 1:  # line item name
            pass

        else:
            for j, p in enumerate(parts):
                if p == "":
                    p = np.nan
                else:
                    try:
                        p = float(p)
                    except:
                        p = p

                data[j].append(p)

    dict_tmp = {columns[i]: data[i] for i in range(len(columns))}
    print(dict_tmp)
    df_tmp = pd.DataFrame(dict_tmp)
    return df_tmp


schedules = [" POR "]
clean_dict1 = dict()
for cyq in raw_dict:
    clean_dict1[cyq] = dict()
    for file_name in raw_dict[cyq]:
        for sched in schedules:
            if sched in file_name:
                path = os.path.join(raw_dir, cyq, file_name)
                # print(path)
                df = read_text(path)
                # print(df.columns)
                if sched not in clean_dict1[cyq]:
                    clean_dict1[cyq][sched] = list()
                clean_dict1[cyq][sched].append(df)


key = ["IDRSSD"]
rssds = set()
for cyq in clean_dict1:
    for sched in clean_dict1[cyq]:
        for df in clean_dict1[cyq][sched]:
            path = os.path.join(clean_dir, f"{cyq}_{sched}.csv")
            df.to_csv(path, sep=',', encoding='utf-8', index=False)