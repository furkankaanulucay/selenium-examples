from selenium import webdriver
from userInfo import mail, password
import time
import xlsxwriter
from selenium.webdriver import ChromeOptions
import re
CLEANR = re.compile('<.*?>') 

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-web-security")
options.add_argument("--disable-popup-blocking")

class Firefox:
    def __init__(self):
        self.browser = webdriver.Chrome(options=options, executable_path = r'C:\Users\pc\Downloads\chromedriver.exe')
        self.sayac = 1 # global sayac degeri tanımlıyoruz.
    
    def veriCek(self,worksheet):
        #eskisi testEl = self.browser.find_elements_by_xpath("//*[@id='main-content']/section[1]/div[1]")
        testEl = self.browser.find_element_by_xpath("//*[@id='main-content']/section[1]")
        testVal = testEl.find_elements_by_css_selector(".mzp-l-content")
        for i in range(1,len(testVal) + 1):
            isIt = self.browser.find_element_by_xpath(f"//*[@id='main-content']/section[1]/div[{i}]/div[1]").find_elements_by_tag_name("h3")
            if(len(isIt) > 0):
                innerVal = self.browser.find_element_by_xpath(f"//*[@id='main-content']/section[1]/div[{i}]/div[1]/h3").get_attribute("innerHTML")
                version = self.browser.find_element_by_xpath("//*[@id='main-content']/header/div/div[2]/div[1]/h2/div[1]").get_attribute("innerHTML")
                date = self.browser.find_element_by_xpath("//*[@id='main-content']/header/div/div[2]/div[1]/p").get_attribute("innerHTML")
                if(innerVal and innerVal == 'New'):
                    new = self.browser.find_element_by_xpath(f"//*[@id='main-content']/section[1]/div[{i}]/div[2]/ul")
                    elem2 = new.find_elements_by_tag_name("li")
                    for x in range(0,len(elem2)):
                        elem2[x] = re.sub(CLEANR, '', f'{elem2[x].get_attribute("innerHTML")}')
                        worksheet.write(f'A{self.sayac}', f'{version}') # versiyon yazılıyor.
                        worksheet.write(f'B{self.sayac}', 'New') # new,changed,fixed gibi değerler yazılıyor.
                        worksheet.write(f'C{self.sayac}', f'{date}') # tarih yazılıyor.
                        worksheet.write(f'D{self.sayac}', f'{elem2[x]}') # içerik yazılıyor.
                        self.sayac+= 1
                if(innerVal and innerVal == 'Changed'):
                    new = self.browser.find_element_by_xpath(f"//*[@id='main-content']/section[1]/div[{i}]/div[2]/ul")
                    elem2 = new.find_elements_by_tag_name("li")
                    for x in range(0,len(elem2)):   

                        elem2[x] = re.sub(CLEANR, '', f'{elem2[x].get_attribute("innerHTML")}')
                        worksheet.write(f'A{self.sayac}', f'{version}')
                        worksheet.write(f'B{self.sayac}', 'Changed')
                        worksheet.write(f'C{self.sayac}', f'{date}')
                        worksheet.write(f'D{self.sayac}', f'{elem2[x]}')
                        self.sayac+= 1
                if(innerVal and innerVal == 'Fixed'):
                    new = self.browser.find_element_by_xpath(f"//*[@id='main-content']/section[1]/div[{i}]/div[2]/ul")
                    if(new):
                        elem2 = new.find_elements_by_tag_name("li")
                        for x in range(0,len(elem2)):    

                            elem2[x] = re.sub(CLEANR, '', f'{elem2[x].get_attribute("innerHTML")}')
                            worksheet.write(f'A{self.sayac}', f'{version}')
                            worksheet.write(f'B{self.sayac}', 'Fixed')
                            worksheet.write(f'C{self.sayac}', f'{date}')
                            worksheet.write(f'D{self.sayac}', f'{elem2[x]}')
                            self.sayac+= 1

    def signIn(self,workbook,worksheet):
        self.browser.get("https://www.mozilla.org/en-US/firefox/releases/")
        time.sleep(1)
        release = self.browser.find_element_by_xpath("//*[@id='main-content']/ol")
        release_count = release.find_element_by_tag_name("li")
        for i in range(1,62):
            self.browser.find_element_by_xpath(f"//*[@id='main-content']/ol/li[{i}]/strong/a").click()
            time.sleep(2)
            self.veriCek(worksheet)
            time.sleep(1)
            self.browser.back()
            sec_counts = self.browser.find_element_by_xpath(f"//*[@id='main-content']/ol/li[{i}]")
            if(len(sec_counts.find_elements_by_tag_name("ol")) >= 1):
                second_relase = self.browser.find_element_by_xpath(f"//*[@id='main-content']/ol/li[{i}]/ol")
                sec_count = second_relase.find_elements_by_tag_name("li")
                print(sec_count)
                if(len(sec_count) > 0):
                    # child menu kontrol 5.0.1 gibi.
                    for j in range(1,(len(sec_count) + 1)):
                        self.browser.find_element_by_xpath(f"//*[@id='main-content']/ol/li[{i}]/ol/li[{j}]/a").click()
                        time.sleep(2)
                        self.veriCek(worksheet)
                        # sayac+=1
                        time.sleep(1)
                        self.browser.back()
            # print("burda self.sayac")
            # print(self.sayac)
        workbook.close()

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
firefox = Firefox()
firefox.signIn(workbook,worksheet)