from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from jep_config import *
from scraper.helpers import clean_data

driver = webdriver.Chrome()

driver.get(SEASON_LIST)

def get_answers():
    """
    returns a list of all answers on current page
    """
    correct_responses = []

    try:
        answers = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "correct_response"))
        )
        for answer in answers:
            cleaned = clean_data(answer)
            correct_responses.append(cleaned)
    except TimeoutException as e:
            print("Error! {}".format(e))

    return correct_responses


for i in range(1, CURRENT_SEASON):
    text = "Season {}".format(i)

    try:
        # click into the current season
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )
        print("Clicking into {} link!".format(element.text))
        element.click()

        # grab a list of links for all games found in the season
        games_list = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "aired"))
        )

        games_list[0].click()

        answer_list = get_answers()
        for answer in answer_list:
            print(answer)

    except TimeoutException as e:
        print(e)
