from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import functools as ft
from tabulate import tabulate

options = Options()
options.headless = True

path = '/Users/sujay/Downloads/chromedriver_mac_arm64/chromedriver' #introduce your file's path inside '...'

driver = webdriver.Chrome(path)

web = 'https://app.prizepicks.com/'
driver.get(web)

time.sleep(10)

accept = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[3]/button')
accept.click()

time.sleep(1)

nba = driver.find_element_by_xpath('//*[@id="board"]/div[1]/div/div/div[1]') # last number should be the nba column
nba.click()

pp_players = []
pp_props = []

projections = driver.find_elements_by_class_name('projection')

for projection in projections:
    pp_players.append(projection.find_element_by_class_name('name').text)
    pp_props.append(projection.find_element_by_class_name('score').text)

# for i in range(len(players)):
#     print("player:", pp_players[i], "prop:", pp_props[i])

time.sleep(5)

# draft kings
web = 'https://sportsbook.draftkings.com/leagues/basketball/nba?category=player-points'
driver.get(web)

time.sleep(5)

dk_players = []
dk_props_o = []
dk_props_u = []
players = driver.find_elements_by_class_name('sportsbook-row-name')
props = driver.find_elements_by_class_name('sportsbook-outcome-cell')

for player in players:
    dk_players.append(player.text)

for prop in props:
    a = prop.find_element_by_class_name('sportsbook-outcome-cell__label').text
    b = prop.find_element_by_class_name('sportsbook-outcome-cell__line').text
    c = prop.find_element_by_css_selector("span[class='sportsbook-odds american default-color']").text
    if (a == "O"):
        dk_props_o.append(str(a + b + " " + c))
    else:
        dk_props_u.append(str(a + b + " " + c))

# for j in range(len(dk_players)):
#     print("dk player:", dk_players[j], "dk prop", dk_props_o[j], dk_props_u[j])

# points bet

web = 'https://nj.pointsbet.com/sports/basketball/NBA'
driver.get(web)

time.sleep(10)

pb_players = []
pb_props_o = []
pb_props_u = []

games = driver.find_elements_by_class_name('f8xi195')

for i in range(len(games)):
    games = driver.find_elements_by_class_name('f8xi195')
    b = games[i]
    driver.execute_script('arguments[0].click();', b)
    time.sleep(10)

    button = driver.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[2]/button')
    driver.execute_script('arguments[0].click();', button)
    time.sleep(5)
    button2 = driver.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]/button')
    driver.execute_script('arguments[0].click();', button2)
    time.sleep(5)

    players = driver.find_elements_by_class_name('fqltveq')
    for player in players:
        pb_players.append(player.find_element_by_class_name('f1i87hcv').text.title())
        a = player.find_elements_by_css_selector("span[class='f5rl2hl']")
        b = player.find_elements_by_css_selector("span[class='fheif50']")
        o = a[0].text.split()
        u = a[1].text.split()

        pb_props_o.append("O" + o[-1] + " " + b[0].text)
        pb_props_u.append("U" + u[-1] + " " + b[1].text)

    driver.back()
    time.sleep(5)

# combine

pp_data = {"player": pp_players,
        "pp prop": pp_props,}

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
df_final = ft.reduce(lambda left, right: pd.merge(left, right, on='player', how='left'), dfs)

# merged_table = pd.merge(left=pp, right=dk, on='player')

print(tabulate(df_final, headers='keys', tablefmt='github'))

# driver.close()