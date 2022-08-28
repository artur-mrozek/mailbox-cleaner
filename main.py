from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def deleteO2Mails():
    driver = webdriver.Chrome()
    driver.get("https://poczta.o2.pl/login/login.html")
    driver.find_element("xpath", "//button[text()='AKCEPTUJĘ I PRZECHODZĘ DO SERWISU']").click()
    driver.find_element("id", "login").send_keys(input("Email address: "))
    driver.find_element("id", "password").send_keys(input("Password: ") + Keys.ENTER)
    driver.find_elements()

    while len(driver.find_elements("xpath", "//button[text()='Folder Odebrane jest pusty']")) == 0:
        driver.find_element("xpath", "//*[contains(text(), 'Zaznacz wszystkie')]").click()
        time.sleep(0.5)
        driver.find_element("name", "delete-20px").click()
        time.sleep(0.5)
        if len(driver.find_elements("xpath", "//*[contains(text(), 'Tak, przenoszę wszystkie wiadomości')]")) != 0:
            driver.find_element("xpath", "//*[contains(text(), 'Tak, przenoszę wszystkie wiadomości')]").click()
        time.sleep(1.5)

    while True:
        time.sleep(1)


if __name__ == '__main__':
    deleteO2Mails()
