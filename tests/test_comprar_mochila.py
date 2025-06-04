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

    # Inicia o Sauce Labs Appium Driver
    driver = webdriver.Remote("https://oauth-difarmo-6859d:43bdf5b4-9473-4911-aea3-e46fcdddaa26@ondemand.us-west-1.saucelabs.com:443/wd/hub", options=options)

    wait = WebDriverWait(driver, 1) # cria uma instância de espera explícita com timeout de 1 segundo
    driver.implicitly_wait(2) # configura o tempo de espera implícito para 1 segundo

    # Blocos de código para interagir com o aplicativo
    lblSecao = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="title")
    assert lblSecao.text == "Products"
    imgMochila = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"Product Image\"])[1]")
    imgMochila.click()

    # time.sleep(1)
    el3 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/productTV")
    el3.click()
    # wait.until(EC.presence_of_element_located((
    #     AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV"))).click()

    lblNomeProduto = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/productTV")
    assert lblNomeProduto.text == "Sauce Labs Backpack"
    lblPrecoProduto = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV")
    assert lblPrecoProduto.text == "$ 29.99"
    sltCor = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Black color")
    sltCor.click()
    txtQuantidade = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV")
    txtQuantidade.click()
    btnAdicionarNoCarrinho = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to add product to cart")
    btnAdicionarNoCarrinho.click()
    lblQuantidadeNoCarrinho = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(3)")
    lblQuantidadeNoCarrinho.click()
    
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(530, 1993)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(541, 1202)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
        
    # Destroir o driver após o teste
    driver.quit()