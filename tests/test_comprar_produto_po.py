import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
 
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
def test_comprar_mochila():
    options = AppiumOptions()
    options.load_capabilities({
        # # Configurações do Appium para o dispositivo físico Android
        # "platformName": "Android",
        # "appium:platformVersion": "13.0",
        # "appium:deviceName": "emulator5554",
        # "appium:deviceOrientation": "portrait",
        # "appium:appPackage": "com.saucelabs.mydemoapp.android",
        # "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity",
        # "appium:automationName": "UiAutomator2",
        # "browserName": "",
        # "appium:ensureWebviewsHavePages": True,
        # "appium:nativeWebScreenshot": True,
        # "appium:newCommandTimeout": 3600,
        # "appium:connectHardwareKeyboard": True

        # Configuracao para o Sauce Labs
        "platformName": "Android",
        "appium:platformVersion": "13.0",
        "appium:deviceName": "emulator5554",
        "appium:app": "storage:filename=mda-2.2.0-25.apk",
        "appium:deviceOrientation": "portrait",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity",
        "appium:automationName": "UiAutomator2",
        "browserName": "",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })
    
    # Inicia o Appium Server antes de executar este teste
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    wait = WebDriverWait(driver, 1) # cria uma instância de espera explícita com timeout de 1 segundo