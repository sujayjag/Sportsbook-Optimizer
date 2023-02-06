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

average_o = []
average_u = []
optimizer = []

for row in df.iterrows():
    data = []
    for i in range(0, len(df.axes[1])):
        data.append(str(row[1][i]))
    if "nan" in data:
        data = [i for i in data if i != "nan"]

    o = []
    u = []

    for j in range(2, len(data), 2):
        over = data[j].split()
        over[1] = int(over[1])
        over[0] = float(over[0][1:])
        o.append(over)
        
        under = data[j+1].split()
        under[1] = int(under[1])
        under[0] = float(under[0][1:])
        u.append(under)

    sum = 0
    sum2 = 0
    count = 0
    diff = False
    for i in range(len(o)):
        sum += o[i][1]
        sum2 += u[i][1]
        count += 1

        if float(o[i][0]) != float(data[1]):
            diff = True

    if diff:
        average_o.append("diff lines")
        average_u.append("diff lines")
        optimizer.append(-300)
    else:
        average_o.append(sum/count)
        average_u.append(sum2/count)
        optimizer.append(min(sum/count, sum2/count))

calc = {"player": pp_players,
        "average o" : average_o,
        "average u" : average_u,
        "min" : optimizer}

c = pd.DataFrame(calc)

df_final = pd.merge(left=df, right=c, on='player')
df_final = df_final.sort_values(by='min')

print(tabulate(df_final, headers='keys', tablefmt='github'))