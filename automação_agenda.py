import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = uc.Chrome()

driver.get('https://accounts.google.com/ServiceLogin?hl=pt-BR&passive=true&continue=https://www.google.com/&ec=GAZAmgQ')
login = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
login.send_keys('diasgame006@gmail.com')
login.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
senha = driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
senha.send_keys('diasgamerbr0220')
senha.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
# nova aba
driver.execute_script("window.open('https://calendar.google.com/calendar/u/0/r?pli=1')")
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(10)

driver.close()
driver.quit()