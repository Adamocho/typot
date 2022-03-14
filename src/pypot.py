"""TypeRacer "Fair Play" Bot"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def main():
    PATH = "C:\\Dev\\chromedriver.exe"

    with open('path.txt') as path:
        PATH = path.read()

    driver = webdriver.Chrome(PATH)

    # Change it in the future
    driver.get("https://play.typeracer.com/")

    try:
        practices = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "gwt-Anchor"))
        )
        # print(practice.text)
        # practice.click()

        iterator = 0

        for pracitce in practices:
            # print(iterator)
            # print(pracitce.text)
            iterator += 1

            if iterator == 5:
                pracitce.click()
                break

        panel = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inputPanel"))
        )
        # print(panel.text) # to be sure that this is FULL TEXT
        content = panel.text[:-21]
        print(content)

        time.sleep(4)

        textBar = driver.find_element_by_class_name("txtInput")
        for chars in content:
            textBar.send_keys(chars)
            time.sleep(random.randrange(5, 10)/500) # more legit
            # time.sleep(2/100) # less legit

    finally:
        time.sleep(5)
        driver.quit()
        print("QUITED")

if __name__ == '__main__':
    main()