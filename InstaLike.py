import time 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class InstaLikeBot():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
    
    def startLikes(self, profileLink, user, passwd):
        self.driver.get('https://www.instagram.com/')
        sleep(7)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(user)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(passwd)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
        print("LOGGED IN")
        sleep(4)
        self.driver.get(profileLink)
        print("INSIDE PROFILE")
        sleep(4)
        totPosts = int(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span').text)
        print("The total posts are: ")
        print(totPosts)
        elem = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[1]')
        actions = ActionChains(self.driver)
        actions.move_to_element(elem).click().perform()
        sleep(7)
        i = 1
        while i <= totPosts:
            actions = ActionChains(self.driver)
            doubleTapArea = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div')
            actions.double_click(doubleTapArea).perform()
            print("Double Tapped post no. "+str(i))
            sleep(1)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.RIGHT)
            i+=1
            sleep(5)
            



bot = InstaLikeBot()
user = 'YOUR USER NAME HERE'
passwd = 'YOUR HERE'

favPerson = 'vaishnavi_ganesh_nayaka'

bot.startLikes('https://www.instagram.com/'+favPerson+'/', user, passwd)