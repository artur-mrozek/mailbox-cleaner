from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


def deleteO2Mails():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://poczta.o2.pl/login/login.html")
    time.sleep(1)  # wait for cookie prompt
    driver.find_element("xpath", "//button[text()='AKCEPTUJĘ I PRZECHODZĘ DO SERWISU']").click()
    driver.find_element("id", "login").send_keys(input("Email address: "))
    driver.find_element("id", "password").send_keys(input("Password: ") + Keys.ENTER)
    time.sleep(3)  # wait for log in

    while len(driver.find_elements("xpath", "//button[text()='Folder Odebrane jest pusty']")) == 0:
        driver.find_element("xpath", "//*[contains(text(), 'Zaznacz wszystkie')]").click()
        time.sleep(0.5)
        driver.find_element("name", "delete-20px").click()
        time.sleep(0.5)
        if len(driver.find_elements("xpath", "//*[contains(text(), 'Tak, przenoszę wszystkie wiadomości')]")) != 0:
            driver.find_element("xpath", "//*[contains(text(), 'Tak, przenoszę wszystkie wiadomości')]").click()
        time.sleep(1.5)
    print("done")


def deleteWPMails():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://profil.wp.pl/login/login.html")
    time.sleep(1)  # wait for cookie prompt
    driver.find_element("xpath", "//button[text()='AKCEPTUJĘ I PRZECHODZĘ DO SERWISU']").click()
    driver.find_element("id", "login").send_keys(input("Email address: "))
    driver.find_element("id", "password").send_keys(input("Password: ") + Keys.ENTER)
    time.sleep(3)  # wait for log in

    while len(driver.find_elements("xpath", "//button[text()='Folder Odebrane jest pusty']")) == 0:
        driver.find_element("xpath", "//nh-checkbox[@aria-label='Zaznacz wiadomości']").click()
        time.sleep(1)
        driver.find_element("xpath", "//*[contains(text(), 'usuń')]").click()
        time.sleep(1)
        if len(driver.find_elements("xpath", "//button[@data-sel-elem='modal_empty_trash_accept']")) != 0:
            driver.find_element("xpath", "//button[@data-sel-elem='modal_empty_trash_accept']").click()
        time.sleep(2)
    print("done")


if __name__ == '__main__':
    while True:
        option = input("Type\no2 - clear o2 mailbox\nwp - clear wp mailbox\nexit - exit programm\n")
        if option == "wp":
            deleteWPMails()
        elif option == "o2":
            deleteO2Mails()
        elif option == "exit":
            break
        else:
            print("Type correct input")
