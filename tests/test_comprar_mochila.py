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
 
def test_comprar():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "13.0",
        "appium:deviceName": "emulator5554",
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
    
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(1) # configura o tempo de espera implícito para 1 segundo
    wait = WebDriverWait(driver, 1) # cria uma instância de espera explícita com timeout de 1 segundo

    lblSecao = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="title")
    lblSecao.click()
    imgMochila = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"Product Image\"])[1]")
    imgMochila.click()

    # time.sleep(5)
    el3 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/productTV")
    el3.click()
    # wait.until(EC.presence_of_element_located((
    #     AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV"))).click()

    el4 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Black color")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV")
    el6.click()
    el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to add product to cart")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(3)")
    el8.click()
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(530, 1944)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(545, 1224)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(530, 1993)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(541, 1202)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
        
        
    driver.quit()
