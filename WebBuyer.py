from selenium import webdriver

class WebBuyer():

    website = "dumb_website"

    def load_website(website):
        WebBuyer.website = website
        return website
    
    def get_website():
        return WebBuyer.website
    
    def ping_website():
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(chrome_options=chrome_options)

        driver.get(WebBuyer.get_website())

        if driver.current_url == WebBuyer.get_website():
            return "accessible"

        else:
            return "inaccessible"