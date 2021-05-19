from selenium import webdriver

class WebBuyer():

    website = "dumb_website"

    def load_website(website):
        WebBuyer.website = website
        return website
    
    def get_website():
        return WebBuyer.website