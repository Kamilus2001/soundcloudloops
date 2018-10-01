from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time
#in this file i was trying to make loop. Final code is in final.py file
location = 'your_chrome_driver_direction'
driver = webdriver.Chrome(location)
driver.get('https://soundcloud.com/teamsesh/bones-tempo-prod-by-eric-dingus')
#"//div[@class='playbackTimeline__timePassed']"
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".playbackTimeline__duration")))
    f = open("file.txt", "w")
    f.write(element.text)
    f.close()
    f = open("file.txt", "r")
    i = 0
    minutes = ""
    seconds = ""
    for line in f.readlines():
        if(i==1):
            timedata = line
        i +=1
    f.close()
    for x in timedata:
        if i<=3:
            if x!=":":
                minutes += str(x)
        elif i>=4:
            if x != ":":
                seconds += str(x)
        i += 1
    minutes = int(minutes)
    seconds = int(seconds)
    minutes *= 60
    minutes += seconds
    czas = time()
    while True:
        if time() - czas > minutes:
            driver.refresh()
            czas = time()
finally:
    pass

#box = soup.find('div', {'class': 'upcoming challenge-list'})
