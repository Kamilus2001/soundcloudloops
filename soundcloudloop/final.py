from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time

class SCLOOP(object):
    def __init__(self, pagelink):
        self.link = pagelink
        location = 'D:/chromedriver/chromedriver.exe'
        self.driver = webdriver.Chrome(location)
        self.driver.get(self.link)
        self.minutes = ""
        self.seconds = ""
        self.CountSeconds()
    def CountSeconds(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".playbackTimeline__duration")))
        except Exception:
            pass
        f = open("file.txt", "w")
        f.write(element.text)
        f.close()
        f = open("file.txt", "r")
        i = 0
        for line in f.readlines():
            if (i == 1):
                timedata = line
            i += 1
        f.close()
        for x in timedata:
            if i <= 3:
                if x != ":":
                    self.minutes += str(x)
            elif i >= 4:
                if x != ":":
                    self.seconds += str(x)
            i += 1
        self.minutes = int(self.minutes)
        self.seconds = int(self.seconds)
        self.minutes *= 60
        self.minutes += self.seconds
        element = 0

    def loopsong(self):
        czas = time()
        while True:
            if time() - czas> self.minutes:
                self.driver.refresh()
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//a[@class='sc-button-play playButton sc-button m-stretch']"))).click()
                except Exception:
                    pass
                czas = time()
                element = 0
    def exit(self):
        self.driver.quit()
#to loop song faster do this \/
strona  = SCLOOP('https://soundcloud.com/tadeusz-kowalski-714978308/killem-all/s-HCHfm').loopsong()