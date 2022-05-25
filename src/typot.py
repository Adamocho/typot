"""TypeRacer "Fair Play" Bot"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def main():

    # What is this joke?
    PATH = ""
    with open('path.txt') as path:
        PATH = path.readlines() if len(path.read())  else "C:\\Dev\\chromedriver.exe"


    PATH = "C:\\Dev\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # Change it in the future
    driver.get("https://play.typeracer.com/")

    try:
        # For later use
        modes = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "gwt-Anchor"))
                )

        # modes[1].click()

        panel = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inputPanel"))
                )
        # Take text from the text field
        content = panel.text[:-22]

        # Wait for the text field to unlock
        time.sleep(4)

        textBar = driver.find_element_by_class_name("txtInput")

        # I know that there is a bot support, so every keypress has a random factor added,
        # So it is considered "more legit"
        for chars in content:
            textBar.send_keys(chars)
            time.sleep(random.randrange(5, 10)/500) # more legit
            # time.sleep(2/100) # less legit
    finally:
        pass
        time.sleep(5)
        # driver.quit()

if __name__ == '__main__':
    main()