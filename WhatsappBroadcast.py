import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WhatsappHelper():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def sendMessage(self, number, message):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        for num in number:
            script = "window.open('https://web.whatsapp.com/send?phone=%s&text=%s', 'new window')" % (num, message)
            self.driver.execute_script(script)
            time.sleep(3)
            tabs = self.driver.window_handles
            time.sleep(3)
            self.driver.switch_to.window(tabs[1])
            time.sleep(5)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
            time.sleep(3)


bot = WhatsappHelper()
number = ['+91964744235', '+91583853853'] #Enter all numbers here
msg = 'Hello!' #Enter your message here
bot.sendMessage(number, msg)

