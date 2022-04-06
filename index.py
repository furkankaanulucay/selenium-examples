from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


option = Options()

option.add_argument("--disable-infobars")

option.add_argument("start-maximized")

option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 }) 
driver = webdriver.Chrome(executable_path = r'C:\Users\pc\Downloads\chromedriver.exe')
driver.get("https://www.hepsiburada.com/")

print("site başlığı: " + driver.title)
element_to_hover_over = driver.find_element_by_id("myAccount")

hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
time.sleep(3)
# driver.find_element_by_id("login").click()
driver.quit()