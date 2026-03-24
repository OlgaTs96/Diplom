from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PersonalPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_button(self):
        wait = WebDriverWait(self.driver, 30)
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//span[text()="Добавить проект с задачами"]')
        ))
        button.click()

    def create_new_prod(self, value):
        wait = WebDriverWait(self.driver, 30)
        name_prod = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Введите название проекта…']")
        ))
        name_prod.clear()
        name_prod.send_keys(value)

        add_prod = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[text()='Добавить проект с задачами']")))
        add_prod.click()
