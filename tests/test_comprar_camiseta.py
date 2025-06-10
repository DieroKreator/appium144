from appium.options.common.base import AppiumOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

def test_comprar_camiseta():

    options = AppiumOptions()
    options.load_capabilities({

        # Configurações do Appium para o dispositivo físico Android
        "platformName": "Android",
        "appium:platformVersion": "13.0",
        "appium:deviceName": "emulator5554",
        "appium:deviceOrientation": "portrait",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity",
        "appium:automationName": "UiAutomator2",
        "browserName": "",
        "appium:ensureWebviewsHavePages": True
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    lblSecao = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="title")
    assert lblSecao.text == "Products"

    driver.quit()