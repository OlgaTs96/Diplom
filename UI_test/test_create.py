import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from pages.MainPage import MainPage
from pages.PersonalPage import PersonalPage
import os

load_dotenv()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def auth_page(driver):
    return MainPage(driver)


def test_create_prod(auth_page):
    auth_page.go_to_login_page()
    auth_page.login_as(os.getenv("login"), os.getenv("password"))
    WebDriverWait(auth_page.driver, 30).until(
        EC.url_to_be("https://ru.yougile.com/team/"))
    personal_page = PersonalPage(auth_page.driver)
    personal_page.click_button()
    personal_page.create_new_prod('Diplom')

    wait = WebDriverWait(auth_page.driver, 30)
    diplom_element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Diplom')]")
    ))

    assert diplom_element is not None
