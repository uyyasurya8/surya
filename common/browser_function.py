

class Browser:
    def __init__(self,driver):
        self.driver = driver

    def validation_message(self):
        validation_message = self.driver.locator('[data-testid="login-email-input"]').evaluate("element => element.validationMessage")
        print("Validation Message :", validation_message)
        assert validation_message == "Please fill out this field."