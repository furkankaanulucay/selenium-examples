from selenium import webdriver
from userInfo import mail, password
import time
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-web-security")
options.add_argument("--disable-popup-blocking")

class HepsiBurada:
    def __init__(self):
        self.browser = webdriver.Chrome(options=options, executable_path = r'C:\Users\pc\Downloads\chromedriver.exe')
    
    def signIn(self):
        self.browser.get("https://humanbenchmark.com/tests/aim")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='root']/div/div[4]/div[1]/div/div[1]/div[2]").click()
        for i in range(30):
            self.browser.find_element_by_xpath("//*[@id='root']/div/div[4]/div[1]/div/div[1]/div/div/div").click()

hepsiburada = HepsiBurada()
hepsiburada.signIn()