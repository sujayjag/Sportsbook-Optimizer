from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create a new instance of the Chrome driver with headless option
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get("https://app.prizepicks.com/")

# Find all the elements with class "name"
names = driver.find_elements_by_css_selector(".projection .proj-container .player-container .player .name")

# Extract the text from each element
all_names = [name.text for name in names]

# Print the names
print(all_names)

# Close the browser
driver.quit()
