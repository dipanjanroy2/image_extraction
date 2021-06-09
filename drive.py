from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

val = input("Enter the link: ")
driver = webdriver.Chrome(chrome_options=chrome_options)
#open the webpage
driver.get(val)

time.sleep(5)
#images = []  
    
for j in range(0,1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

    #target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
anchors = [a for a in anchors if str(a).startswith(val)]

print('Found ' + str(len(anchors)) + ' links to images')

images = []

#follow each image link and extract only image at index=1
for a in anchors:
    driver.get(a)
    time.sleep(2)
    img = driver.find_elements_by_tag_name('a')
    img = [i.get_attribute('href') for i in img]
    img = [a for a in anchors if str(a).startswith(val)]
    images.append(img[4])




duration = 1  # seconds
freq = 100  # Hz
os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
os.system('spd-say "hey dude your program has finished"')

#@TheHatedOne
# @UN5TABLE
