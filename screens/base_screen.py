class BaseScreen:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return self.driver.find_element(by, value)
    
    def find_elements(self, by, locator, value):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(value)

    def click_element(self, by, locator):
        self.find(by, locator).click()

    def get_text (self, by, locator):
        return self.find(by, locator).text
    
    def is_displayed(self, by, locator):
        try:
            return self.find(by, locator).is_displayed()
        except:
            return False