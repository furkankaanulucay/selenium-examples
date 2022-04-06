from selenium import webdriver
from userInfo import mail, password
import time
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-web-security")
options.add_argument("--disable-popup-blocking")

class HumanBenchmark:
    def __init__(self):
        self.browser = webdriver.Chrome(options=options, executable_path = r'C:\Users\pc\Downloads\chromedriver.exe')
        self.started = False
    
    def continueStep(self):
        test = self.browser.find_elements_by_class_name("css-19b5rdt")
        for i in range(1,len(test)):
            key = test[i]
            j = i-1
            while j >= 0 and int(key.get_attribute('data-cellnumber')) < int(test[j].get_attribute('data-cellnumber')):
                test[j + 1] = test[j]
                j -= 1
            test[j + 1] = key
        time.sleep(2)
        if(self.started == True):
            print("girdim2")
            test[0].click()
            time.sleep(1)
            test2 = self.browser.find_elements_by_class_name('css-10qtjsi')
            time.sleep(1)
            for i in range(1,len(test2)):
                key2 = test2[i]
                j = i-1
                while j >= 0 and int(key2.get_attribute('data-cellnumber')) < int(test2[j].get_attribute('data-cellnumber')):
                    test2[j + 1] = test2[j]
                    j -= 1
                test2[j + 1] = key2
            time.sleep(2)
            for i in range(0,len(test2)):
                test2[i].click()
                time.sleep(1)
            time.sleep(2)
            self.checkStep()
        else:
            print("geldimmm")
            for i in range(0,len(test)):
                print(test[i].get_attribute('data-cellnumber'))
            for i in range(0,len(test)):
                test[i].click()
                time.sleep(1)
            self.started = True
            self.checkStep()
            
    def startTest(self):
        self.browser.get("https://humanbenchmark.com/tests/chimp")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='root']/div/div[4]/div[1]/div/div[1]/div[2]/button").click()
        time.sleep(1)
        self.continueStep()
        
    
    

    def checkStep(self):
        time.sleep(2)
        if(self.browser.find_element_by_xpath("//*[@id='root']/div/div[4]/div[1]/div/div[1]/div[3]/button")):
            self.browser.find_element_by_xpath("//*[@id='root']/div/div[4]/div[1]/div/div[1]/div[3]/button").click()
            self.continueStep()



humanBenchmark = HumanBenchmark()
humanBenchmark.startTest()