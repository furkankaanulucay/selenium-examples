from selenium import webdriver
from userInfo import mail, password
import time
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-web-security")
options.add_argument("--disable-popup-blocking")

class HepsiBurada:
    def __init__(self,mail,password):
        self.browser = webdriver.Chrome(options=options, executable_path = r'C:\Users\pc\Downloads\chromedriver.exe')
        self.mail = mail
        self.password = password
    
    def signIn(self):
        self.browser.get("https://giris.hepsiburada.com/?ReturnUrl=https%3A%2F%2Foauth.hepsiburada.com%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DSPA%26redirect_uri%3Dhttps%253A%252F%252Fwww.hepsiburada.com%252Fuyelik%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%26state%3Db20ece9d59db4d3990ea65f6dbb0defc%26code_challenge%3DRvVwGJImX4PnHRaat_YktHeHwq1tGQCQDZTB5-J5f80%26code_challenge_method%3DS256%26response_mode%3Dquery%26ActivePage%3DPURE_LOGIN%26oidcReturnUrl%3Dhttps%253A%252F%252Fwww.hepsiburada.com%252F")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='txtUserName']").send_keys(self.mail)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='btnLogin']").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='txtPassword']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='btnEmailSelect']").click()
        time.sleep(2)
        self.browser.get("https://hepsiburada.com")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='myAccount']").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='myAccount']/div/div[2]/ul/li[3]/a").click()
        time.sleep(3)
        self.browser.find_element_by_link_text("Adreslerim").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='customer-addresses']/div/div/div/ul/li[1]/a").click()
        time.sleep(2)
        self.browser.find_element_by_name("firstName").send_keys("Kaan")
        time.sleep(1)
        self.browser.find_element_by_name("lastName").send_keys("Uluçay")
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[3]/div/div/button").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[3]/div/div/div/ul/li[2]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[4]/div/div/button").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[4]/div/div/div/ul/li[2]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='address']").send_keys("ŞeyhŞamil Mah. Baytem Siteleri")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='address-name']").send_keys("Evim")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='phone']").send_keys("5538589058")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='form-address']/div/div/div[2]/div/button").click()

hepsiburada = HepsiBurada(mail,password)
hepsiburada.signIn()