from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('http://seleniumhq.org/')

print(driver.current_url)
