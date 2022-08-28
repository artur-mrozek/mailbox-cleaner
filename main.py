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

    time.sleep(5)

if __name__ == '__main__':
    deleteO2Mails()
