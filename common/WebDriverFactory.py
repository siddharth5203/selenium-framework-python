from selenium import webdriver

class WebDriverFactory:

    def setDriver():
        WebDriverFactory.driver = webdriver.Remote(
        command_executor="http://192.168.1.203:4444/wd/hub",
        desired_capabilities={
            "browserName": "chrome"
        })
        
    def getDriver():
        return WebDriverFactory.driver
