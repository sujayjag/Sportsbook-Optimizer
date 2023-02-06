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
    time.sleep(5)

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

# print(len(pb_players))
# print(len(pb_props_o))
# print(len(pb_props_u))

# for j in range(len(pb_players)):
#     print("pb player:", pb_players[j], "pb prop", pb_props_o[j], pb_props_u[j])

pb_data = {"player": pb_players,
        "pb prop o": pb_props_o,
        "pb prop u": pb_props_u}

pb = pd.DataFrame(pb_data)

print(tabulate(pb, headers='keys', tablefmt='github'))