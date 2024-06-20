from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

season_list = "https://www.j-archive.com/listseasons.php"

driver.get(season_list)

for i in range(1, 41):
    text = "Season {}".format(i)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )
        print("Found {} link!".format(element.text))
    except TimeoutException as e:
        print(e)
