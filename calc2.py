from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import functools as ft
from tabulate import tabulate
import statistics

pp_players = ["Darius Garland", "Jimmy Butler", "Evan Mobley"]
pp_props = [21.5, 20.5, 14.5]

dk_players = ["Darius Garland", "Jimmy Butler", "Evan Mobley"]
dk_props_o = ["O21.5 -110", "O20.5 -115", "O13.5 -140"]
dk_props_u = ["U21.5 -120", "U20.5 -115", "U13.5 +110"]

pb_players = ["Darius Garland", "Evan Mobley"]
pb_props_o = ["O21.5 -110", "O14.5 -105"]
pb_props_u = ["U21.5 -120", "U14.5 -125"]

pp_data = {"player": pp_players,
        "pp prop": pp_props}

dk_data = {"player": dk_players,
        "dk prop o": dk_props_o,
        "dk prop u": dk_props_u}

pb_data = {"player": pb_players,
        "pb prop o": pb_props_o,
        "pb prop u": pb_props_u}

pp = pd.DataFrame(pp_data)
dk = pd.DataFrame(dk_data)
pb = pd.DataFrame(pb_data)

dfs = [pp, dk, pb]
df = ft.reduce(lambda left, right: pd.merge(left, right, on='player', how='left'), dfs)

optimizer = [0, 0, 0]

# for index, row in df.iterrows():
#     print(row["pb prop o"])
#     if str(row["pb prop o"]) == "nan":
#         print("NANAANAANAN")

# for col in df:
#     rows = (df[col].values)
#     for row in rows:
#         print(row)

# lines = []

# for col in df:
#     print((df[col].values)[0])

for row in df.iterrows():
#     data = [row[1][1], row[1][2]]
    data = []
    for i in range(0, len(df.axes[1])):
        data.append(str(row[1][i]))
    print(data)
    if "nan" in data:
        print("WAAAAA")

calc = {"player": pp_players,
        "optimizer": optimizer}

c = pd.DataFrame(calc)

df_final = pd.merge(left=df, right=c, on='player')

print(tabulate(df_final, headers='keys', tablefmt='github'))