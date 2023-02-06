from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# web = 'https://sports.tipico.de/en/all/football/spain/la-liga' #you can choose any other league

options = Options()
options.headless = True

web = 'https://app.prizepicks.com/'
path = '/Users/sujay/Downloads/chromedriver_mac_arm64/chromedriver' #introduce your file's path inside '...'

driver = webdriver.Chrome(path)
driver.get(web)

time.sleep(5)

print("sup")

accept = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[3]/button')
accept.click()

next = driver.find_element_by_xpath('//*[@id="board"]/div[1]/div/div/div[3]')
next.click()

cards = driver.find_elements_by_class_name('score')

for card in cards:
    print(card.text)

time.sleep(5)

driver.close()