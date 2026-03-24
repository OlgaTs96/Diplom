from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage():
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.get('https://ru.yougile.com/')
        self._wait = WebDriverWait(driver, 10)

    def click_login_button(self):
        login_btn = self._wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.btn-outline-primary')))
        login_btn.click()

    def authorization_username(self, email):
        email_input = self._wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "//input[@type='email']")))
        email_input.clear()
        email_input.send_keys(email)

    def authorization_password(self, password):
        password_input = self._wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='password']")))
        password_input.clear()
        password_input.send_keys(password)
        submit_btn = self._wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".hint__cnt")))  # Исправлено
        submit_btn.click()
