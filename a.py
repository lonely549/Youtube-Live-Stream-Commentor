import self as self
from selenium import webdriver
from time import sleep


class Google:

    def __init__(self, username, password):
        self.driver = webdriver.Chrome (
            'Link of chromedriver')
        self.driver.get ('https://stackoverflow.com/users/signup')
        sleep (3)
        self.driver.find_element_by_xpath ('//*[@id="openid-buttons"]/button[1]').click ()
        self.driver.find_element_by_xpath ('//input[@type="email"]').send_keys (username)
        self.driver.find_element_by_xpath ('//*[@id="identifierNext"]').click ()
        sleep (3)
        self.driver.find_element_by_xpath ('//input[@type="password"]').send_keys (password)
        self.driver.find_element_by_xpath ('//*[@id="passwordNext"]').click ()
        sleep (2)
        link = str (input ("Enter the URL of the live Video:"))
        self.driver.get (link)
        sleep (3)
        self.driver.find_element_by_xpath ('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]').click ()
        sleep (3)
        print ('Liked The Video')
        sleep(3)
        #self.driver.find_element_by_xpath ('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer').click ()#
       # print ('subscribed channel')
        link = str (input ("Enter the Youtube live chat popup link of the Youtube Video: "))
        self.driver.get(link)
        sleep(3)
        self.driver.find_element_by_xpath ('//*[@contenteditable=""]').click ()
        sleep (1)
        self.driver.find_element_by_xpath ('//*[@contenteditable=""]').send_keys ('Bro help needed')
        sleep(1)
        self.driver.find_element_by_xpath ('//*[@contenteditable=""]').send_keys (u'\ue007')
        sleep(2)
        print ('comment sucess- lonely pwoliyane')
        sleep(15)



passw = open ('1.txt', "r", encoding="utf-8")
password = str (passw.read ())
user = open ('2.txt', "r", encoding="utf-8")
username = str (user.read ())
mylike = Google (username, password)
