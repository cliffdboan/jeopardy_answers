from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()

season_39 = "https://www.j-archive.com/showseason.php?season=39"

browser.get("https://www.j-archive.com/showgame.php?game_id=8342")

def clean_data(answer):
    """Strip the answers of any excess characters:
    "A", "The", "<i>", "&"

    Args:
        answer (html): should be a single jepoardy answer in the form of an html tag
    """
    cleaned = answer.get_attribute("innerHTML")
    cleaned = cleaned.replace("&amp;", "")
    cleaned = cleaned.replace("<i>", "")
    cleaned = cleaned.replace("</i>", "")
    cleaned = cleaned.strip('"')
    cleaned = cleaned.lower()
    return cleaned

try:
    answers = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "correct_response"))
    )
    for answer in answers:
        cleaned = clean_data(answer)
        print(cleaned)
finally:
    browser.quit()
