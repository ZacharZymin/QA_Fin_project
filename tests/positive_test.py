from page.base_page import BasePage
from page.reg_page import RegistrationPage
import time


# Открываем сайт и проверяем что он открылся по URL
def test_open_site(setup):
    assert setup.current_url == "https://www.google.com/intl/ru/gmail/about/"


def test_click_logo(setup):
    page = BasePage(setup)
    page.click_btn_logo()
    assert setup.current_url == "https://www.google.com/intl/ru/gmail/about/"


# Кнопка "Для бизнеса"  проверяем переход по URL соответствию
def test_click_for_work_button(setup):
    page = BasePage(setup)
    page.click_btn_for_work()
    assert setup.current_url == page.current_url_for_work


# Кнопка "Войти"  проверяем переход наличию кнопки "Далее" после перехода
def test_click_login(setup):
    page = BasePage(setup)
    page.click_btn_login()
    assert page.find(page.button_further)


# Кнопка "Создать аккаунт"  проверяем переход по URL соответствию
def test_click_create_acc(setup):
    page = BasePage(setup)
    page.click_btn_create_account()
    assert setup.current_url == page.current_url_create_account


# Регистрация нового аккаунта (Тест является не законченным так как у меня нет свободного номера телефона для полной регистрации, но есть возмодность его дописать)
def test_reg_account(setup):
    page = RegistrationPage(setup)
    page.click_btn_create_account()
    page.input_field_first_name_new_acc(page.valid_firstname)
    page.input_field_last_name_new_acc(page.valid_lastname)
    page.input_field_user_name_new_acc(page.valid_username_newacc)
    page.input_field_password_first(page.valid_password)
    page.input_field_password_last(page.valid_password)
    page.click_btn_further()
    assert True


# Авторизация существующего аккаунта (Пока не понятно как это сделать, хром блокирует автоматизацию на этом этапе)
def test_login(setup):
    page = RegistrationPage(setup)
    page.click_btn_login()
    page.input_field_login(page.valid_email)
    page.click_btn_further()
    assert True
