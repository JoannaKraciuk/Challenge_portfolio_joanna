import os
import time
import unittest
import pytest
import allure
from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from util.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://dareit.futbolkolektyw.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @allure.title('Log in to dashboard page')
    @allure.description('This test execute login to the dashboard page with valid data')
    def test_login_page(self):

        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        element_text = BasePage(self.driver)
        element_text.assert_element_text(self.driver, '//div/h5', 'Scouts Panel')
        user_login.type_in_email('user10@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()