from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Set up Selenium webdriver (make sure to install the appropriate driver for your browser)
options = Options()
#options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument('--disable-gpu') 
# options.add_argument("--disable-extensions")
options.add_argument("--log-level=3")  # fata
driver = webdriver.Chrome("./chromedriver.exe", options=options)


# Loop over the assets and perform the actions on each one
for asset_num in range(200, 965):
    asset_url = f"https://opensea.io/assets/arbitrum/0x02692941aaa28e03c2bc0cc460a6f4f40b319077/{asset_num}"
    print(f"Processing asset {asset_url}")
  
    # Load the asset page
    driver.get(asset_url)

    # Wait for the More button to be clickable and then click it
    more_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="More"]'))
    )
    more_button.click()

    # Wait for the list of items to appear and click the first one
    list_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.sc-d8be1725-0'))
    )
    list_item.click()
    print("^^ Refreshed ^^")
    time.sleep(4)


# Close the webdriver
driver.quit()
