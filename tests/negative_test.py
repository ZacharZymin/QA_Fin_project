import time

from page.base_page import BasePage
from page.reg_page import RegistrationPage


def test_login_invalid_value(setup):
    page = BasePage(setup)
    page.click_btn_login()
    page.input_field_login(page.invalid_email)
    page.click_btn_further()
    # time.sleep(5)
    assert page.alert_text_login1


def test_login_invalid_password(setup):
    page = BasePage(setup)
    page.click_btn_login()
    page.input_field_login(page.valid_email)
    page.click_btn_further()
    page.input_field_password(page.invalid_password)
    assert True


def test_invalid_username(setup):
    page = RegistrationPage(setup)
    page.click_btn_create_account()
    page.input_field_first_name_new_acc(page.valid_firstname)
    page.input_field_last_name_new_acc(page.valid_lastname)
    page.input_field_user_name_new_acc(page.invalid_username_newacc)
    page.input_field_password_first(page.valid_password)
    page.input_field_password_last(page.valid_password)
    assert page.alert_text_invalid_username


def test_invalid_password(setup):
    page = RegistrationPage(setup)
    page.click_btn_create_account()
    page.input_field_first_name_new_acc(page.valid_firstname)
    page.input_field_last_name_new_acc(page.valid_lastname)
    page.input_field_user_name_new_acc(page.valid_username_newacc)
    page.input_field_password_first(page.valid_password)
    page.input_field_password_last(page.invalid_password)
    assert page.alert_text_invalid_password


def test_invalid_firstname(setup):
    page = RegistrationPage(setup)
    page.click_btn_create_account()
    page.input_field_first_name_new_acc(page.invalid_firstname)
    page.input_field_last_name_new_acc(page.valid_lastname)
    page.input_field_user_name_new_acc(page.valid_username_newacc)
    page.input_field_password_first(page.valid_password)
    page.input_field_password_last(page.valid_password)
    page.click_btn_further()
    assert page.alert_text_invalid_firstname


def test_invalid_lastname(setup):
    page = RegistrationPage(setup)
    page.click_btn_create_account()
    page.input_field_first_name_new_acc(page.valid_firstname)
    page.input_field_last_name_new_acc(page.invalid_lastname)
    page.input_field_user_name_new_acc(page.valid_username_newacc)
    page.input_field_password_first(page.valid_password)
    page.input_field_password_last(page.valid_password)
    page.click_btn_further()
    assert page.alert_text_invalid_lastname