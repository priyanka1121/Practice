from time import sleep

from selenium import webdriver


browser = webdriver.Firefox()

browser.implicitly_wait(5)


browser.get('https://www.instagram.com/accounts/login/?hl=en')


login_link = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form')
login_link.click()


sleep(2)


username_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input ')

password_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input ')


username_input.send_keys("coder_2x")

password_input.send_keys("OD19IE")


login_button = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
login_button.click()

notnow_button = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
notnow_button.click()

turnoff_button = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
turnoff_button.click()

sleep(15)


browser.close()