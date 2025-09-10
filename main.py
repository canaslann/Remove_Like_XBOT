from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.ie.service import Service

# msedgedriver yolunu buraya yaz (örnek: "C:/tools/msedgedriver.exe")
edge_driver_path = "C:/msedgedriver.exe"


service = Service(edge_driver_path)

driver = webdriver.Edge(service=service)
driver.maximize_window()

driver.get("https://twitter.com/login")
time.sleep(3)

username = driver.find_element(By.NAME, "text")
username.send_keys("ENTER_USERNAME")
username.send_keys(Keys.RETURN)
time.sleep(2)

password = driver.find_element(By.NAME, "password")
password.send_keys("ENTER_PASSWORD")
password.send_keys(Keys.RETURN)
time.sleep(5)

driver.get("https://twitter.com/ENTER_USERNAME/likes")
time.sleep(5)

control = True
sayac = 0
while control:
    try:
        unlike_button = driver.find_element(By.XPATH, "//button[@data-testid='unlike']")
        unlike_button.click()
        print("Beğeni kaldırıldı")
        time.sleep(3)  # çok hızlı olursa ban riski var
        driver.execute_script("window.scrollBy(0, 50);")
    except:
        print("Buton bulunamadı, sayfa kaydırılıyor...")
        sayac += 1
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(3)
        if sayac == 30:
            control = False

driver.quit()
