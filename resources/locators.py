from selenium.webdriver.common.by import By


class PageLocators:
    # Базовая страница
    button_login = (By.XPATH, "//a[contains(text(), 'Войти')]")
    button_forwork = (By.XPATH, "//header/div[1]/div[1]/div[1]/a[1]")
    button_create_account = (By.XPATH, "//header/div[1]/div[1]/div[1]/a[3]/span[2]")
    button_change_account = (By.XPATH, "//div[contains(text(),'Сменить аккаунт')]")
    button_logout = (By.XPATH, "//a[contains(text(), 'Войти')]")
    button_logo = (By.XPATH, "/html/body/header/div/a")

    # Регистрация
    field_firstname = (By.XPATH, "//*[@id='firstName']")
    field_lastname = (By.XPATH, "//*[@id='lastName']")
    field_username = (By.XPATH, "//input[@id='username']")
    field_first_password = (By.XPATH, "//*[@id='passwd']/div[1]/div/div[1]/input")
    field_last_password = (By.XPATH, "//*[@id='confirm-passwd']/div[1]/div/div[1]/input")
    button_further = (By.XPATH, "//span[contains(text(),'Далее')]")
    alert_text_invalid_username = (By.LINK_TEXT, "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.).")
    alert_text_invalid_password = (By.LINK_TEXT, "Пароли не совпадают. Повторите попытку.")
    alert_text_invalid_firstname = (By.LINK_TEXT, "Проверьте правильность своих имени и фамилии.")
    alert_text_invalid_lastname = (By.LINK_TEXT, "Проверьте правильность своих имени и фамилии.")

    field_email = (By.XPATH, "//input[@type='email']")
    field_password = (By.XPATH, "//input[@type='password']")

    # Логин
    alert_text_login = (By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div/text()")
    alert_text_login1 = (By.LINK_TEXT, "Введите адрес электронной почты или номер телефона.")
    login_password_field = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
