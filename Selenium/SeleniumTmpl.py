"""
A Template for a basic Selenium project
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    driver = webdriver.Chrome()
    # go to  https://sites.google.com/chromium.org/driver/
    # click Downloads
    # download the version of Chrome Driver that matches your version of Chrome
    # and move to the venv/bin folder
    # To find your version of Chrome: Settings > About Chrome

    driver.get("https://www.google.com")

    # To get an XPath:
    # right click > Inspect
    # Locate field (Input, button, etc) by expanding collapsed divs
    # right click > copy > copy full XPath
    # paste between quotes like in this template:
    # driver.find_element_by_xpath("")
    element = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    element.send_keys("Hello World!")  # Search Hello World on Google

    element2 = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    element2.click()

    time.sleep(300)  # for staying on web page


if __name__ == "__main__":
    main()

