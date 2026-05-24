

class Browser:
    def __init__(self,driver):
        self.driver = driver

    def validation_message(self):
        validation_message = self.driver.locator('[data-testid="login-email-input"]').evaluate("element => element.validationMessage")
        print("Validation Message :", validation_message)
        assert validation_message == "Please fill out this field."


class Browser_1:
    def __init__(self,driver):
        self.driver = driver

    def validation_message(self):
        validation_message = self.driver.locator('[data-testid="login-email-input"]').evaluate("element => element.validationMessage")
        print("Validation Message :", validation_message)
        assert validation_message == "Please include an '@' in the email address. 'uno.test' is missing an '@'."


class Browser_2:
    def __init__(self,driver):
        self.driver = driver

    def validation_message(self):
        validation_message = self.driver.locator('[data-testid="login-email-input"]').evaluate("element => element.validationMessage")
        print("Validation Message :", validation_message)
        assert validation_message == "'.' is used at a wrong position in 'gmail.'."