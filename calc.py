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

pb_players = ["Darius Garland", "Jimmy Butler", "Evan Mobley"]
pb_props_o = ["O21.5 -110", "O20.5 -115", "O14.5 -105"]
pb_props_u = ["U21.5 -120", "U20.5 -115", "U14.5 -125"]

# pb_players = ["Darius Garland", "Evan Mobley"]
# pb_props_o = ["O21.5 -110", "O14.5 -105"]
# pb_props_u = ["U21.5 -120", "U14.5 -125"]

average_o = []
average_u = []
optimizer = []
for x in range(len(pp_players)):
    dk = dk_props_o[x].split()
    print(dk)
    dk_line = float(dk[0][1:])
    print(dk_line)

    pb = pb_props_o[x].split()
    pb_line = float(pb[0][1:])

    o = []
    o.append(int(dk_props_o[x][-4:]))
    o.append(int(pb_props_o[x][-4:]))

    u = []
    u.append(int(dk_props_u[x][-4:]))
    u.append(int(pb_props_u[x][-4:]))

    if pp_props[x] == dk_line and pp_props[x] == pb_line:
        a_o = sum(o) / len(o)
        a_u = sum(u) / len(u)

        average_o.append(a_o)
        average_u.append(a_u)

        optimizer.append(min(a_o, a_u))
    else:
        s = statistics.stdev([pp_props[x], dk_line, pb_line])
        s = ((2+s)/2)
        average_o.append("n/a")
        average_u.append("n/a")
        if pp_props[x] == dk_line:
            optimizer.append(s*int(dk_props_o[x][-4:]))
        else:
            optimizer.append(s*int(pb_props_o[x][-4:]))

pp_data = {"player": pp_players,
        "pp prop": pp_props}

dk_data = {"player": dk_players,
        "dk prop o": dk_props_o,
        "dk prop u": dk_props_u}

pb_data = {"player": pb_players,
        "pb prop o": pb_props_o,
        "pb prop u": pb_props_u}

calc = {"player": pp_players,
        "average o" : average_o,
        "average u" : average_u,
        "optimizer" : optimizer}

pp = pd.DataFrame(pp_data)
dk = pd.DataFrame(dk_data)
pb = pd.DataFrame(pb_data)
c = pd.DataFrame(calc)

dfs = [pp, dk, pb, c]
df_final = ft.reduce(lambda left, right: pd.merge(left, right, on='player', how='left'), dfs)
df_final = df_final.sort_values(by='optimizer')

print(tabulate(df_final, headers='keys', tablefmt='github'))