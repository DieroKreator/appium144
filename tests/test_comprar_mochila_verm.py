import time
from appium.options.common.base import AppiumOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_comprar_mochila_verm():

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
    driver.implicitly_wait(2) # configura o tempo de espera implícito para 1 segundo
    wait = WebDriverWait(driver, 1)

    lblSecao = wait.until(EC.presence_of_element_located(
           (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='title']")))
    # lblSecao = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="title")
    assert lblSecao.text == "Products"
    mochilaVermLabel = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Sauce Labs Backpack (red)\")")
    assert mochilaVermLabel.text == "Sauce Labs Backpack (red)"
    mochilaVermPrice = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.saucelabs.mydemoapp.android:id/priceTV\").instance(3)")
    assert mochilaVermPrice.text == "$ 29.99"
    imgMochilaVerm = driver.find_element(AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"Product Image\"])[4]")
    imgMochilaVerm.click();
    lblSecaoProduto = wait.until(EC.presence_of_element_located(
           (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productTV")')))
    assert lblSecaoProduto.text == "Sauce Labs Backpack (red)"
    lblPrecoProduto = driver.find_element(AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV")
    assert lblPrecoProduto.text == "$ 29.99"

    # # To fix the color selection, we need to ensure the correct color is selected.
    # sltCor = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value="Red color");
    # sltCor.click();

    txtQuantidade = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV")
    assert txtQuantidade.text == "1"
    btnAddCarrinho = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value="Tap to add product to cart")
    btnAddCarrinho.click()
    lblQuantidadeNoCarrinho = wait.until(EC.presence_of_element_located(
           (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/cartTV")')))
    assert lblQuantidadeNoCarrinho.get_attribute("text") == "1"
    lblQuantidadeNoCarrinho.click()

    lblSecaoCarrinho = wait.until(EC.presence_of_element_located(
           (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")))
    assert lblSecaoCarrinho.text == "My Cart"
    lblNomeProdutoCarrinho = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/titleTV")
    assert lblNomeProdutoCarrinho.text == "Sauce Labs Backpack (red)"
    lblPrecoProdutoCarrinho = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV")
    assert lblPrecoProdutoCarrinho.text == "$ 29.99"
    btnFinalizarCompra = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Confirms products for checkout")
    btnFinalizarCompra.click()

    lblSecaoLogin = wait.until(EC.presence_of_element_located(
           (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/loginTV"]')))
    assert lblSecaoLogin.text == "Login"
    txtUsuario = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/nameET")
    txtUsuario.send_keys("bod@example.com")
    txtSenha = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/passwordET")
    txtSenha.send_keys("10203040")
    btnLogin = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to login with given credentials")
    btnLogin.click()

    lblSecaoCheckout1 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/checkoutTitleTV")
    assert lblSecaoCheckout1.text == "Checkout"
    txtNome = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/fullNameET")
    txtNome.send_keys("David Reynolds")
    txtEndereco = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/address1ET")
    txtEndereco.send_keys("123 Main St, Springfield, USA")
    txtCidade = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cityET")
    txtCidade.send_keys("Springfield")
    txtEstado = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/stateET")
    txtEstado.send_keys("IL")
    txtCep = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/zipET")
    txtCep.send_keys("62701")
    txtPais = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/countryET")
    txtPais.send_keys("USA")        
    btnContinuar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Saves user info for checkout")
    btnContinuar.click()

    lblSecaoCheckout2 = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV")
    assert lblSecaoCheckout2.text == "Enter a payment method"
    txtCardName = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/nameET")
    txtCardName.send_keys("David Reynolds")
    txtCardNumber = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cardNumberET")
    txtCardNumber.send_keys("4111111111111111")
    txtCardExpiry = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/expirationDateET")
    txtCardExpiry.send_keys("12/25")
    txtCardCvv = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/securityCodeET")
    txtCardCvv.send_keys("123")
    btnRevisarOrdem = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Saves payment info and launches screen to review checkout data")
    btnRevisarOrdem.click()

    lblSecaoRevisao = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/enterShippingAddressTV")
    assert lblSecaoRevisao.text == "Review your order"
    lblNomeProdutoRevisao = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/titleTV")
    assert lblNomeProdutoRevisao.text == "Sauce Labs Backpack (red)"
    lblPrecoProdutoRevisao = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV")
    assert lblPrecoProdutoRevisao.text == "$ 29.99"
    lblQuantidadeProdutos = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/itemNumberTV")
    assert lblQuantidadeProdutos.text == "1 Items"
    btnFinalizarCompra = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Completes the process of checkout")
    btnFinalizarCompra.click()

    lblSecaoFinalizacao = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/completeTV")
    assert lblSecaoFinalizacao.text == "Checkout Complete"
    msgFinalizacao = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/thankYouTV")
    assert msgFinalizacao.text == "Thank you for your order"
    btnVoltarAoInicio = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to open catalog")
    btnVoltarAoInicio.click()

    lblSecaoCatalog = wait.until(EC.presence_of_element_located(
           (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='title']")))
    assert lblSecaoCatalog.text == "Products"

    driver.quit()