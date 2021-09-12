"""
A selenium template that uses a class to house driver functionality
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Example:
    def __init__(self, url):
        # Set up driver and load webpage, then wait to ensure everything loads
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        time.sleep(2)

    def destroy(self):
        # Close browser window
        self.driver.close()

    def search(self, query):
        # Add methods to define repeated functionality
        sb_path = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        search_bar = self.driver\
            .find_element_by_xpath(sb_path)
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.ENTER)


def main():

    # go to  https://sites.google.com/chromium.org/driver/
    # click Downloads
    # download the version of Chrome Driver that matches your version of Chrome
    # and move to the venv/bin folder
    # To find your version of Chrome: Settings > About Chrome

    bot = Example("https://www.google.com")
    bot.search("Hello World")

    time.sleep(10)
    bot.destroy()


if __name__ == "__main__":
    main()
